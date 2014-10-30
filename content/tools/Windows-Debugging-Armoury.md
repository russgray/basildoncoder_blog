Title: Windows Debugging Armoury
Date:
Author: Russell Gray
Slug: windows-debugging-armoury
Tags: coding, .net
Status: draft

Searching around the web will reveal a number of debugging setup guides. There
are lots of little tips and tricks that you pick up through a career of
figuring out why your production code is misbehaving, and it's helpful to jot
it all down in one place.

> This is my toolkit. There are many like it, but this one is mine.

More specifically, this is for dealing with .Net applications on Windows. I
might create something similar for dealing with java on Linux at some point.

# Install List
- [Windows Driver Kit 8.1][1] (requires VS2013). WDK 8 is no longer supported.
- [SOSEX 4][2]
- [Psscor4 Managed-Code Debugging Extension for WinDbg][3]

Alternatively, you can download [my zip file][4] of these tools. They don't
require installation, just copy it where you need it. Of course, if you don't
trust me, get them from source. And get permission from your friendly sysadmin
before putting this stuff on a production box.

# Set-up Symbols
Create directories on a disk with a couple gig free space:

	mkdir C:\Symbols
	mkdir C:\SymbolCache

Create the following environment variables:

	_NT_SYMBOL_PATH=SRV*C:\Symbols*http://msdl.microsoft.com/download/symbols
	_NT_SYMCACHE_PATH=C:\SymbolCache

Add any local/app symbols. For instance if you have an application and
associated PDB files in `C:\temp\PDB`:

	C:\> "C:\Program Files (x86)\Windows Kits\8.0\Debuggers\x86\symstore" add /f "C:\temp\PDB\*.*" /s c:\Symbols /t "Debuggable Server"
	C:\> "C:\Program Files (x86)\Windows Kits\8.0\Debuggers\x86\symstore" query /s c:\Symbols /f C:\temp\PDB\Server.exe

Add `C:\Program Files (x86)\Windows Kits\8.0\Debuggers\x86` to your path if
you expect to use `symstore` frequently.

For more information on symstore, check out the [symstore docs][5].aspx).

Also see [Setting Yourself up for Debugging][6] at Thomas Kejser's Database
Blog.

# Profiling

[Windows Performance Recorder]7] in conjunction with Windows Performance
[Analyzer is an insanely powerful way of profiling performance of .Net
[applications in production without the overhead of more traditional code
[profilers. It is analogous to dtrace on *nix systems.

For looking at kernel context switches (indicative of blocking calls and lock
contention), open `Computation -> CPU Usage (Precise) -> Context Switch Count
by Process, Thread`. Rearrange the columns so that `NewProcessName`,
`NewThreadStack`, `ReadyingProcess`, and `ReadyThreadStack` are to the left of
the thick yellow line. Sort descending by `Waits (us)` on the right. Select
`Load Symbols` from the Trace menu. This will take a while, but once done you
can drill down into your code and see exactly where threads are being switched
back in and what happened to allow them to continue (e.g. which line of code
was blocking, and which line of code unblocked it).

With a bit of practice, this is like having the Eye of freakin' Sauron glaring
at your code for you. Coarse-grained locks deep in the .Net framework itself
are dragged kicking and screaming into the sunlight. Awful connection pool
management in your database driver is held up for all to see. No-one escapes.

# Debugging

Production debugging is a tricky beast. If you have a route through the
network and some off-peak time, you can connect with Visual Studio's remote
debugger. This can kill performance though. For memory problems, you can just
as usefully grab a process dump and debug it on your own workstation at your
leisure.

## Start WinDbg

Open crash dump file (Ctrl-D)

Load sos.dll:

	.loadby sos clr

Try running a SOS command, e.g. `!threads`. If it fails with a 'load data
access DLL' error, it's probably the wrong version of SOS (even the revision
numbers have to match). Follow the instructions and run `.cordll -ve -u -l` to
check, and if necessary grab SOS.dll from the dump machine (typical path
`C:\Windows\Microsoft.NET\Framework64\v4.0.30319`)

Load psscor4:

	.load <PATH_TO_PSSCOR4.DLL>

Load sosex.dll:

	.load <PATH_TO_SOSEX.DLL>

Set up symbol path. If you have a local symstore (as above), use:

	.sympath srv*c:\symbols*http://msdl.microsoft.com/download/symbols

If you just have an app directory containing PDBs, use:

	.sympath srv*http://msdl.microsoft.com/download/symbols
	.sympath+ "C:\Program Files\DeployedServer"

Reload modules:

	.reload /f

Toggle debug info with:

	!sym noisy
	!sym quiet

Enable DML:

	.prefer_dml 1

[Further symbol path info][8]

## Using WinDbg

WinDbg is not what you'd call beginner-friendly. The following pages have some
useful lists of commands in addition to those I've covered below.

- http://windbg.info/doc/1-common-cmds.html
- http://msdn.microsoft.com/en-us/library/bb190764.aspx
- http://theartofdev.wordpress.com/windbg-cheat-sheet/

### Info

Command | Description | Example
--- | --- | ---
`x` | display symbols | `x clr!Thread::*`


### Threads/Execution

Command | Description
--- | ---
`!threads` | Display all threads
`.shell -ci "!threads" findstr 15` | pipes output of !threads into findstr, useful for e.g. looking up a managed thread ID (OSID) to find the thread ID that can be used with `~s`
`~22s` | switch debugger to thread ordinal 22
`~~[12AB]s` | switch to managed thread ID 0x12AB
`!pe` | dump exception on current thread
`!clrstack` | dump managed stack
`!mk` | dump managed and native stack
`!do` | dump object
`!sosex.dlk` | search for deadlocks
`!sosex.mlocks` | search for threads holding locks
`!sosex.mwaits` | search for threads waiting on locks
`!psscor4.syncblk` | run command for all threads
`!eestack -short -EE` | todo
`~*e!\<command\>` | run command for all threads
`!psscor4.dumpallexceptions` | todo
`!sosex.mframe` | set current frame for !mdv
`!sosex.mdv` | display arguments and parameters for current frame

### Memory
Command | Description
--- | ---
`!dumpheap stat` | heap stats
`!dumpheap type MyAssembly.MyClass statistics` | heap for given type


[1]: http://msdn.microsoft.com/en-us/windows/hardware/gg454513.aspx
[2]: http://www.stevestechspot.com/SOSEXV40NowAvailable.aspx
[3]: http://www.microsoft.com/en-gb/download/details.aspx?id=21255
[4]: https://www.dropbox.com/s/15a26wbldqrke3y/debugging-toolkit.zip
[5]: http://msdn.microsoft.com/en-us/library/windows/desktop/ms681378\(v=vs.85\
[6]: http://kejser.org/setting-yourself-up-for-debugging/
[7]: http://msdn.microsoft.com/en-us/library/windows/hardware/hh448205.aspx
[8]: http://www.windowstipspage.com/symbol-server-path-windbg-debugging/
