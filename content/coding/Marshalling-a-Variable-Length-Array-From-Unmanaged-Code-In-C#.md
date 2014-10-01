Title: Marshalling a Variable-Length Array From Unmanaged Code In C#
Date: 2009-03-31 20:03
Author: Russell Gray
Slug: Marshalling-a-Variable-Length-Array-From-Unmanaged-Code-In-CSharp

I recently spent time working on some C# code to interact with a simple
[DNS-SD][1] system. This requires using [DNS TXT records][2],
which are not supported in the  [System.Net.Dns][3] class. After a few
google searches failed to turn up a pure .Net client library that met my
needs, I settled on an approach based around p/invoking the Win32
[DnsQuery][4] function.

And quickly ran into problems.

For DNS TXT records, DnsQuery returns a [DNS_TXT_DATA][5] structure
in the Data field of the [DNS_RECORD][6] structure. DNS_TXT_DATA is
declared like this:

    :::c
    typedef struct {
        DWORD dwStringCount;
        PWSTR pStringArray[1];
    } DNS_TXT_DATA,
     *PDNS_TXT_DATA;

Using the very handy [P/Invoke Interop Assistant][7], we see that this
struct can be represented like this in managed code:

    :::csharp
    [StructLayout(LayoutKind.Sequential)]
    public struct DNS_TXT_DATA
    {
        /// DWORD->unsigned int
        public uint dwStringCount;

        /// PWSTR[1]
        [MarshalAs(UnmanagedType.ByValArray,
                   SizeConst=1,
                   ArraySubType=UnmanagedType.SysUInt)]
        public IntPtr[] pStringArray;
    }

There is a problem with pStringArray, unfortunately. The
[System.Runtime.InteropServices.Marshal][8] class cannot marshal a variable
length array, as it needs to know in advance how big the array is in order to
allocate memory. That's why the managed structure needs SizeConst specified in
the MarshalAs attribute.

However, if the DNS TXT record data contains multiple quoted strings separated
by whitespace, DnsQuery will return a structure with a variable number of
elements in pStringArray. Since SizeConst is set at compile-time, when we
marshal this into the managed struct defined above, we only get the first
element in our single-element array. Rats.

More googling turned up very little info on dealing with this, though I found
indications that others had run into the same problem without finding a
satisfactory conclusion. DnsQuery is not the only Win32 function that returns
variable-length arrays, and p/invoking any of the others has the same issue.

Simply declaring SizeConst to be bigger than we need - "hey, I know I'll never
get more than 10 or so strings back, so why not declare SizeConst to be 128?"
- is inelegant (hardcoded upper limits, ugh) and doesn't work properly anyway.
Since the struct layout is sequential the marshaller will copy over (e.g.)
128*sizeof(IntPtr) sequential bytes (a total of 512 bytes, in this case).
That much memory was never allocated on the unmanaged side, so we end up with
a load of junk in the tail of pStringArray, and more often than not the
marshaller chokes on this junk and throws an AccessViolationException. Fun.

There IS a way to get round the problem, though. I'm not sure it's the best
way, but it works and seems stable, so I thought I'd throw it out there in
case anyone else can use it (or maybe explain to me why it's an unsafe stupid
thing to do...)

Basically, since we're dealing with sequential memory, we can use
Marshal.PtrToStructure to marshal the DNS_TXT_DATA structure as defined above,
then use pointer arithmetic to gain access to any further data that needs
marshalling.

Pointer arithmetic? Oh yes, even in the safe and secure world of managed code
it's sometimes still necessary to get our hands dirty, and situations like
this illustrate that it will always be valuable to have some hard-earned
Assembly/C/C++ war wounds.

So, assuming we have valid p/invoke declarations and data structures (I've
included a complete source program below), DnsQuery is called like so:

    :::csharp
    var pServers = IntPtr.Zero;
    var ppQueryResultsSet = IntPtr.Zero;
    var ret = DnsQuery(domain,
                       DnsRecordType.TEXT,
                       DnsQueryType.STANDARD,
                       pServers,
                       ref ppQueryResultsSet,
                       IntPtr.Zero);
    if (ret != 0)
        throw new ApplicationException("DnsQuery failed: " + ret);

If we examine the memory location of ppQueryResultsSet (Ctrl-Alt-M,1 or
Debug->Windows->Memory->Memory1 in Visual Studio) we'll see something like the
following (actual address locations may vary - just copy the int value of
ppQueryResultsSet to the Address bar of the memory window):

    0x049E0878  00 00 00 00  ....
    0x049E087C  b8 09 9e 04  ¸.ž.
    0x049E0880  10 00 20 00  .. .
    0x049E0884  19 30 00 00  .0..
    0x049E0888  00 00 00 00  ....
    0x049E088C  00 00 00 00  ....
    0x049E0890  06 00 00 00  ....
    0x049E0894  b8 08 9e 04  ¸.ž.
    0x049E0898  d8 08 9e 04  Ø.ž.
    0x049E089C  f8 08 9e 04  ø.ž.
    0x049E08A0  28 09 9e 04  (.ž.
    0x049E08A4  68 09 9e 04  h.ž.
    0x049E08A8  88 09 9e 04  ˆ.ž.

I've set the column size to 4 here, as most of the values we are dealing with
are 4 bytes in size. This effectively shows one value per line.

The first 6 rows (24 bytes) correspond to the DNS_RECORD structure up
until (but not including) the DNS_TXT_DATA structure in DNS_RECORD's
Data union. We can marshal this first structure without problem:

    :::csharp
    var dnsRecord = (DnsRecord) Marshal.PtrToStructure(
        ppQueryResultsSet, typeof (DnsRecord));

The DNS_TXT_DATA structure starts at address 0x049E0890 in my example. Having
already marshalled the DNS_RECORD structure, now I want a pointer to the
DNS_TXT_DATA structure. I can do this by creating a new pointer at the address
of ppQueryResultsSet plus 24 bytes, and marshalling again:

    :::csharp
    var ptr = new IntPtr(
        ppQueryResultsSet.ToInt32() + Marshal.SizeOf(dnsRecord));
    var txtData = (DNS_TXT_DATA) Marshal.PtrToStructure(
        ptr, typeof (DNS_TXT_DATA));

Because of the definition of DNS_TXT_DATA, this only marshals 8 bytes - 4
bytes for dwStringCount, and 4 bytes for the single element in pStringArray
(an IntPtr). Since we know the memory is sequential, however, this gives us
everything we need - we now know how many strings have been received (6 in
this case, as indicated at 0x049E0890), and the location of the pointer to the
first string (0x049E0894).

With this info, we can marshal all the pointers into an array with a
length of dwStringCount:

    :::csharp
    ptr = new IntPtr(ptr.ToInt32() + sizeof (uint)); // move to first
    var ptrs = new IntPtr[txtData.dwStringCount];    // dest array
    Marshal.Copy(ptr, ptrs, 0, ptrs.Length);

And finally we iterate through those pointers, marshalling the string
pointed at by each:

    :::csharp
    var strings = new List<string>();
    for (var i = 0; i < ptrs.Length; ++i)
    {
        strings.Add(Marshal.PtrToStringAnsi(ptrs[i]));
    }

While the example I've presented here is specific to DnsQuery, the general
approach should be applicable to any situation where you need to marshal a
data structure containing a variable-length array.

[Source code][9]


[1]: http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt
[2]: http://en.wikipedia.org/wiki/List_of_DNS_record_types
[3]: http://msdn.microsoft.com/en-us/library/system.net.dns.aspx
[4]: http://msdn.microsoft.com/en-us/library/ms682016(VS.85).aspx
[5]: http://msdn.microsoft.com/en-us/library/ms682109(VS.85).aspx
[6]: http://msdn.microsoft.com/en-us/library/ms682082(VS.85).aspx
[7]: http://clrinterop.codeplex.com/
[8]: http://msdn.microsoft.com/en-us/library/system.runtime.interopservices.marshal.aspx
[9]: https://gist.github.com/russgray/4748c3f1815f6f2f273d