Title: Packages of the Month (TODO - month!)
Author: Russell Gray
Slug: packages-of-the-month-todo
Tags: coding, .net
Status: draft

Like Scott hanselman's (link)

Irregular

## Fody

## LogLib
This is a really nice little lib that neatly solves a common problem. When you're writing a library of your own, you want to have decent logging code throughout. You could, for instance, use NLog and declare it as a dependency for your package, then anyone who uses your library automatically gets it. That's not very nice if your user doesn't like NLog though, or is already using something else. 

LogLib installs a single source file in your project that provides a generalised logging interface (Debug, Trace, Warn yada yada) but doesn't resolve any logging dependencies until runtime. If NLog is available, it uses it. If log4net is being used instead, it'll do likewise. This is done dynamically so no references to any logging libraries are needed by your code, and your decision isn't forced on your users. 