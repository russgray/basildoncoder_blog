Title: Project Euler Problem 4
Date: 2008-04-22 00:53
Author: Russell Gray
Slug: Project-Euler-Problem-4

***[Problem 4][1]*** is
as follows:

> A palindromic number reads the same both ways. The largest palindrome
> made from the product of two 2-digit numbers is 9009 = 91 × 99.
>
> Find the largest palindrome made from the product of two 3-digit
> numbers.

Bit of an easy one, this. The approach is pretty simple to understand -
first calculate all the products of every pair of numbers between 100
and 999, then filter for the palindromic ones, and finally select the
largest. The only even vaguely tricky bit is determining if the number
is palindromic. The easiest check is to simply convert the number to a
string, and check if the string is equal to itself when reversed.

To shake myself out of C#/python complacency, I decided to write my
first attempt at this in good old C. I'm a bit rusty so this took a few
goes to get right (the shame).

First, I need a string reverse function. For those of us that learned to
program when C and C++ were king (before that upstart Java came long and
ousted languages with pointers from classrooms up and down the land),
this is bread and butter.

    :::c
    char* strrev(char* s) {
        char *s1, *s2;
        char c;

        s1 = s2 = s;
        while (*s2)
            s2++;

        while (s1 < s2) {
            c = *(--s2);
            *s2 = *s1;
            *s1++ = c;
        }
        return s;
    }

If you can't read that, shame on you, go and pick up a copy of
[K&R][2]
and read it until you weep. In the meantime, basically what happens here
is I set pointers to the start (s1) and end (s2) of the original string
(s), then swap the pointed-to characters using a temporary variable (c)
and move both pointers 1 character towards each other. Repeat until they
meet in the middle.

In this day and age of immutable strings, this old friend now feels a
little weird - although I retain (and eventually return) the original
pointer, I have in fact modified the actual string that was passed in.
Contrast this with C's trendy modern progeny, where you can't change a
string at all and have to use a StringB[uilder|uffer] when mutating
strings (unless lousy performance makes you smile, of course).

Still, now it is fairly simple to solve the problem. A nested for loop
will let me calculate all the products, and then I just need to convert
the results to strings and do the palindrome test. I keep track of the
largest palindromic number found so far, and print it at the end.

    :::c
    int main() {
        int i, j;
        int largest = -1;
        char s1[7];
        char s2[7];

        for (i = 100; i < 1000; ++i) {
            for (j = i; j < 1000; ++j) {
                int sum = i * j;
                sprintf(s1, "%d", sum);
                strcpy(s2, s1);
                strrev(s2);
                if (strcmp(s1, s2) == 0 && sum > largest) {
                    largest = sum;
                }
            }
        }

        printf("%d\n", largest);

        return 0;
    }

Note I'm using the much-maligned strcpy function here (the cause of most
of the buffer overflow attacks that were so endemic a few years back),
but since I completely control the input it's no problem. Also note the
use of sprintf to convert the int to a string, and I have to make a copy
of the resulting string since my strrev function is destructive. The
char arrays are of size 7, since the largest possible product in the
problem space is 999*999=998001 which is 6 digits - plus 1 for the null
terminator. Which I didn't forget about at all in my first attempt at
this, nosirree.

To make the code a bit more 'modern' I could do the allocation and copy
in the strrev function, so that the passed-in string remains unchanged
and a new string gets returned, but without a garbage collector to rely
on this potentially leads to memory leaks (since strrev allocates the
memory but relies on the caller to free it - easy to forget!). Anyway,
I'm wallowing in nostalgia here so who cares about modern idioms.

Whilst I chose C for this on a whim, it is (as always) enlightening to
write a little C now and then, as it reminds you of the cost of things
that are often taken for granted. Some people *still* don't understand
why a StringBuilder offers better performance (trust me, I have
interviewed more than a few of them), and are happy to write string
manipulation code using immutable strings that results in countless
allocations and destructions taking place, for no justifiable reason.
Writing some string manipulation (or anything else) in C is a nice way
to regain a bit of insight and perspective if you are spoiled by
quad-core PCs and high-falutin' generational garbage collectors and
smartass runtimes that don't let you write past the end of an array.

So, now we've got a nuts 'n' bolts reference implementation, let's look
at some more exotic approaches.

As regular readers will have noticed by now, I'm fairly keen on LINQ -
so it should be no surprise that C# is my next port of call. I was
amused to recall that the .Net string class lacks a Reverse method so I
had to write my own for this, about 20 minutes after I finished
pontificating about the clean healthy virtue of doing so in C! (I didn't
plan it this way, honest.)

There are of course many ways of writing a string reversal routine, but
rather than attempt to mimic the fairly idiomatic C code above, I did
the simple thing:

    :::csharp
    public static string Reverse(this string s)
    {
        char[] ch = s.ToCharArray();
        Array.Reverse(ch);
        return new string(ch);
    }

Since the Array class contains a Reverse method, I can just convert my
string to an array (of chars), reverse that, then create a new string
from it. Done. Things to meditate on regarding this approach:

1.  It relies on a char array. Strings may look like a native type these
    days, but I have to expose their dark and shameful lineage to get
    the job done here.
2.  The throwback nature of this implementation does not, of course,
    extend as far as modifying the parameter. A new string is returned
    and the original remains intact. The garbage collector will take
    care of deallocation.
3.  This is an extension method on System.String, so I can use it
    naturally on any string.

Whatever faults it may have, it's definitely easier to read than the C
code, since the syntax is much closer to the problem domain. This is a
recurring theme when looking at expressiveness. The C code has to
specify the entire algorithm for reversing the string, whereas here the
Array.Reverse method allows us to ignore the details of *how* the string
is reversed. For the purposes of this problem, we don't really care how
the string is reversed, just that it *is* reversed.

It's still warty, however, in that we have to know to turn the string
into an array first, which may be completely non-intuitive to someone
who's never tangled with C-style strings.

With this minor omission from the .Net libraries sorted, the problem can
be solved with a single compound LINQ query:

    :::csharp
    return (from product in
                (from i in Enumerable.Range(100, 900)
                 from j in Enumerable.Range(i, 1000 - i)
                 select i * j)
            where product.ToString() == product.ToString().Reverse()
            select product)
            .Max();

I think that's pretty concise, and quite readable too. The main thing I
don't like about it is the use of Enumerable.Range, which takes 'start'
and 'count' parameters rather than 'from' and 'to', which would look
more natural in this case.

Parameters aside, it's interesting to note the relative clumsiness of
the twin calls to Enumerable.Range. Back when looking at [problem
1][3],
replacing a for loop with a more declarative alternative made the code
considerably more expressive. In this case, however, I don't think it
helps quite so much. Once again, it's to do with the nature of the
problem domain - a nested for loop is quite a natural way to represent
the process of generating the products, so the benefit of a declarative
approach is less marked.

How to improve it? For fun, lets go the whole hog and make a simple
fluent interface to improve readability of the LINQ query. This is what
we want:

    :::csharp
    return (from product in AllProducts.From(100).To(999)
            where product.ToString() == product.ToString().Reverse()
            select product).Max();

Nifty, huh? Well actually I have my reservations about fluent
interfaces, but it's quite the fashion these days so I thought I'd give
it a chance. The example above is trivial to achieve. On a class called
AllProducts we need a static method called From which acts as a factory
method, and an instance method called To which returns an
`IEnumerable<int>` for use in the LINQ query. The class looks like this:

    :::csharp
    class AllProducts
    {
        private int m_from;
        private AllProducts(int @from)
        {
            m_from = @from;
        }

        public static AllProducts From(int from)
        {
            return new AllProducts(@from);
        }

        public IEnumerable<int> To(int to)
        {
            int inclusiveTo = to + 1; // to is inclusive

            return from i in Enumerable.Range(
                       m_from, inclusiveTo - m_from)
                   from j in Enumerable.Range(i, inclusiveTo - i)
                   select i * j;
        }
    }

Fluent interfaces are definitely this season's black. I heard about a
guy who wrote a mocking library without using fluent interfaces for
expectations, and 500 angry TDD advocates chased him out of the building
with pitchforks.

I'm still a bit wary though, tweedy programmer as I am - I just get a
bit nervous about writing hideously contorted classes with a mixture of
static and instance methods, some returning the this ref, some returning
arbitrary IEnumerables, some acting as factories - and all so the
calling code can prance about in a tailored coat and a cool pair of
shades. A noble goal, to be sure, but is the price too high? I guess
we'll know in a year or two when some maintenance programmer has to try
and debug it.

Enough of the lousy clothes metaphor. To finish up what turned out to be
a longer post than expected, here's an F# solution I hacked together
before getting sidetracked with the whole fluent thing. I read a blog
post
[here][4]
about problem 4 (**warning** - also contains solution to problem 6)
but didn't like it too much. It seems to be quite common when reading
F# code on the web for there to be a reliance on Seq.unfold - I'm not
sure it's always the right tool. Then again, my F# is sketchy at best
for the moment, so maybe I should shut up. For balance, however, this is
my solution without using unfold.

Note first that F#, as a .Net language, also lacks a built-in way to
reverse strings. The implementation is extremely similar to the C#
approach above:

    :::fsharp
    let rev (s:string) =
        let ch = s.ToCharArray()
        let ra = Array.rev ch
        let r = new string(ra)
        r

The actual implementation involves two helpers: a small recursive
function to produce all possible products of the numbers contained in
two lists, and a simple check to see if a string is equal to itself
reversed.

    :::fsharp
    let Euler4 =
        let rec allProducts l1 l2 =
            let mul a lst =
                List.map (fun x -> a * x) lst
            match l1 with
            | [] -> []
            | h::t -> (mul h l2) @ (allProducts t l2)

        let isPalindrome x =
            let str = Int32.to_string x
            str = rev str

With the plumbing in place, we can use the very groovy forward pipe
operator to chain together some very readable code. The only thing to
note in here is the reverse ordering of the parameters in the call to
compare - this is because we want the results in descending order, so
that the largest is at the head of the list and easily accessible with
List.hd.

    :::fsharp
    allProducts [100..999][5]
        |> List.filter isPalindrome
        |> List.sort (fun x y = compare y x)
        |> List.hd


[1]: http://projecteuler.net/index.php?section=problems&id=4
[2]: http://www.amazon.co.uk/C-Programming-Language-2nd/dp/0131103628/
[3]: {filename}/projecteuler/Project-Euler-Problems-1-and-2.md
[4]: http://geekswithblogs.net/Erik/archive/2008/02/18/119727.aspx
[5]: 100..999