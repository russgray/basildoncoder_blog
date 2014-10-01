Title: Test-specific Shims in Production Code
Date: 2008-04-21 13:51
Author: Russell Gray
Slug: Test-specific-Shims-in-Production-Code

We're currently on a fairly major kick to increase automated test
coverage of our software. This doesn't just mean 'get the unit test
coverage up to scratch', it also means we are working towards full
end-to-end integration testing using, amongst other tools, some
front-end automation tools such as
[QTP][1] and
[Selenium][2].

Of course, nothing is ever easy when trying to polish away the tarnish
of ancient code. One particular problem we face regularly is patching up
code that breaks the fragile expectations of some of these automation
tools.

Some of our applications - including the one [I am working to
refactor][3]
- contain UI widgets that use a lot of custom painting routines and
conceal data pretty well. One widget, for instance, needs to display
data with a fast refresh rate and so uses a
[double-buffered][4]
approach to avoid flicker. The data it displays, however, is not stored
anywhere; it is discarded as soon as it is rendered. And since the whole
widget view is rendered as a bitmap and blitted to screen, there's no
convenient hierarchy of panels, labels, text boxes, or any other
standard controls.

This, the Automated QA folks tell me, causes a problem since QTP mainly
works by reflecting on properties exposed by controls to get at their
data. So, if QTP wants to read some data from a text box, it accesses
the Text property of that text box. Simple. But this particular widget
doesn't have the equivalent of a Text property.

This isn't really an oversight from a purely functional point of view,
since no part of the actual application code ever needs to get data from
the widget - it's a display mechanism only, not an interactive widget
like a text box. Data is received from a web service, processed a bit,
and dumped into the widget. The widget is the last object to do anything
with the data - no other part of the app ever needs it again.

Since there are no properties on the widget exposing the data, QTP can't
get at it.

Of course, there are ways to keep QTP happy. We can add a few properties
to the widget and keep some data around in member variables, or we can
write some extensions for QTP that allow it to access some of the
widget's internals. The second way is probably the 'right' way since it
keeps test-related code external to the application code - but it's more
time-consuming, and also has a training cost since most developers
aren't going to be familiar with QTP's API.

This leaves the first option. Traditionally I've always been a bit wary
of having what is effectively test code (since it only exists for
testing purposes) deployed with production code. Furthermore, doesn't it
undermine the tests themselves, since they are dependent on code that
never gets executed in production?

On the other hand, in some instances it may be the more pragmatic thing
to do. It's difficult to justify spending a day or two writing a few
hundred lines of QTP extension code when the same effect can be garnered
by adding a single read-only property. It still doesn't quite sit right
for me though, and I can't find much in the way of authoritative
literature that argues one way or the other.


[1]: http://en.wikipedia.org/wiki/QuickTest_Professional
[2]: http://selenium.openqa.org/
[3]: {filename}/The-P.G.-Wodehouse-Method-Of-Refactoring.md
[4]: http://en.wikipedia.org/wiki/Double_buffering#Double_Buffering_in_Computer_Graphics