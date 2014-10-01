Title: Hackish Monitoring With Python and wevtutil
Date: 2012-09-27 11:06
Author: Russell Gray
Slug: Hackish-Monitoring-With-Python-and-wevtutil

I recently started at a new role and was asked, as a way to get a handle on
part of the codebase, to add some logging and monitoring to a key service that
didn't really tell the world too much about what it was doing - and when it
did speak up, no-one was listening.

*Oh, and could you come up with something by tomorrow please? That would be
great.*

Naturally it takes longer than a day to instrument an entire app, but since
exceptions were being written to the event log I figured we could at least get
some useful stuff from there. So the short-term challenge became finding a way
to collect the event logs from 12 production servers, process them to figure
out what's been happening, and then do it frequently enough that pretty graphs
can be generated.

This of course rules out doing anything with the MMC snap-in, as manually
connecting to 12 boxes every few minutes would be a full-time job in itself.
Powershell seemingly provides a number of possibilities, but I couldn't get
[Get-WmiObject][1] [queries][2] to work, [Get-EventLog][3] wouldn't allow me
to provide authentication credentials for the remote machine, and [Get-
WinEvent][4] almost worked but failed to return the actual log message, even
if I [fiddled with the locale][5]. I want to like Powershell, I really do, but
every time I want to use it I hit bugs or OS compatibility issues.

Recent Windows versions come with a handy tool called [wevtutil][6],
however, which is just what I needed. The following command does exactly what
I want:

    wevtutil qe Application /c:50 /q:"*[System[Provider[@Name='APP_NAME'] and (Level=1 or Level=2) and TimeCreated[timediff(@SystemTime)<300000]]]" /e:Events /r:REMOTE_IP /u:SECURE\\Administrator /f:xml

That gets me a maximum of 50 log entries from the last 5 minutes (300000ms) in
the Application log with the specified log provider, on the specified machine,
in XML format. Phew!

From here, it's fairly simple to write some python to invoke that command,
parse the XML response (so that errors can be categorised, e.g.
database.timeout or network.connectivity), and fire some numbers off to the
wonderful [statsd][7]. Then schedule the script to run every 5 minutes, and we
have some very ghetto error monitoring in almost no time!

Now begins the larger task of adding more detailed diagnostics to the app for
more effective monitoring.

Thanks to [http://blogs.msdn.com/b/ericfitz/archive/2008/07/16/wevtutil-scripting.aspx](http://blogs.msdn.com/b/ericfitz/archive/2008/07/16/wevtutil-scripting.aspx)
and
[http://chentiangemalc.wordpress.com/2011/01/25/script-to-collect-all-event-logs-off-a-remote-windows-7-server-2008-machine/](http://chentiangemalc.wordpress.com/2011/01/25/script-to-collect-all-event-logs-off-a-remote-windows-7-server-2008-machine/)
for ideas on scripting wevtutil.


[1]: http://ss64.com/ps/get-wmiobject.html
[2]: http://www.autmon.com/learn/powershell/powershell-quicktips/learn-powershell-event-log/
[3]: http://ss64.com/ps/get-eventlog.html
[4]: http://ss64.com/ps/get-winevent.html
[5]: http://stackoverflow.com/questions/10534982/powershell-get-winevent-has-no-messsage-data
[6]: http://technet.microsoft.com/en-us/library/cc732848(v=ws.10.aspx)
[7]: https://github.com/etsy/statsd