Title: Visual Studio Logs
Date: 2014-12-05T14:42:53
Author: Russell Gray
Slug: visual-studio-logs
Tags: coding, .net

Suffering from the accursed slow Visual Studio startup problem (which really shouldn't happen on the beefy i7 with 16GB RAM and SSD I use at work), I wanted to dig a little deeper and diagnose it.

From [stackoverflow][1]:

1. Run `devenv /log` and wait for Visual Studio to start up.
2. Close the IDE to close the log/stop logging.
3. Assuming VS2013, this will generate ActivityLog XML and XSL files in `%APPDATA%\Microsoft\VisualStudio\12.0\` (adjust version number if you're using something other than VS2013).

Open `ActivityLog.xml` in a browser, or open `ActivityLog.xsl` in VS itself and execute it (`[CTRL]+[ALT]+[F5]`), choosing `ActivityLog.xml` from the File Open dialog that pops up. This will give you a nicely-formatted HTML report where each step is timestamped, so look for the big gaps to find the things that are slowing you down (yes, it's probably Resharper).

[1]: http://stackoverflow.com/a/3995566