Title: Macros: You Oughta Know
Date: 2009-02-06 15:03
Author: Russell Gray
Slug: Macros-You-Oughta-Know

One of the most useful tools available in any decent text editor is the
macro recorder, but it's criminally underused. It seems most people
either don't know the functionality exists, or simply ignore it. This is
a shame, since it's a great timesaver.

I don't know why macros are so underused. It might be a mindset thing -
it can take a little while to develop the ability to spot repetitive
editing tasks quickly (i.e. not when you're 75% of the way through
thinking *dang, I have to do this again?*), so maybe many people never
quite make the leap.

It's worth it though, because once you get your eye in you see chances
to use macros everywhere.

I had a useful example just yesterday, in which I needed to make a
change to a colossal switch statement (220 branches! Run the
cyclomatic-complexity doohickey on THAT!) and had no unit tests to fall
back on.

If I had to modify (and hopefully refactor) such a huge construct I
wanted to be able to compare before-and-after test results, but I didn't
much fancy hand-cranking a few hundred unit tests.

By recording a temporary macro, however, it took just a couple of
minutes to cover every branch. I've decided to post a detailed
walkthrough of the process here in the hopes that a fairly simple
example will be illustrative for those that don't already lean heavily
on macros.

Note that *this is not an advanced tutorial*. Please refrain from
leaving snarky comments about how macros are so much more powerful than
this - I'm just doing some introductory material here :-)

<p>
Here is a representative snippet of the C\# source. It's part of a
legacy permissioning system that, under certain circumstances, needs to
check for the existence of a permission represented by an enum against a
permission table containing a string-based hierarchy
(application/role/permission). The code I was modifying did the
appropriate conversion:

~~~~ {name="code" language="csharp"}
    case PermissionKey.SecurityParameterManagementAdd:    {        return new string[] {"Security", "ParameterManagement", "Add"};    }    case PermissionKey.SecurityRoleManagementAdd:    {        return new string[] {"Security", "RoleManagement", "Add"};    }    case PermissionKey.SecurityRoleManagementModify:    {        return new string[] {"Security", "RoleManagement", "Modify"};    }    case PermissionKey.SecurityUserManagementDelete:    {        return new string[] {"Security", "UserManagement", "Delete"};    }    case PermissionKey.SecurityPermissionManagementAdd:    {        return new string[] {"Security", "PermissionManagement", "Add"};    }
~~~~

I needed to add a couple of branches to this, but I also wanted to tidy
up the code by removing the superfluous braces, as a precursor to
converting it into something a bit more robust and maintainable. I
wanted unit test coverage to give me confidence that I hadn't mucked up
some logic and inadvertantly granted admin access to the helpdesk
trainee role or something.

So, I copied the entire switch body into Notepad++ (well, vim really,
but I'll pretend it's Notepad++ for the sake of making this post a bit
more accessible) and set to work^[1]^.

Before recording my macro, I needed to do a bit of preprocessing to trim
the code down to just the data I wanted to work with. The following
steps show the 'find' regexes I used (in each case, the value of the
replace field was empty, so these are effectively deletes), and the
effect on the first switch branch from the list above:

<p>
\1) Remove opening and closing braces from every switch branch:

    ^\s+[\{\}]$

<p>
~~~~ {name="code" language="csharp"}
    case PermissionKey.SecurityParameterManagementAdd:        return new string[] {"Security", "ParameterManagement", "Add"};
~~~~

<p>
\2) Remove blanks - TextFX/Edit/Delete Blank Lines

~~~~ {name="code" language="csharp"}
    case PermissionKey.SecurityParameterManagementAdd:        return new string[] {"Security", "ParameterManagement", "Add"};
~~~~

<p>
\3) Remove case statements and leading whitespace:

    ^\s+case\s+

<p>
~~~~ {name="code" language="csharp"}
PermissionKey.SecurityParameterManagementAdd:PermissionKey.SecurityParameterManagementAdd:        return new string[] {"Security", "ParameterManagement", "Add"};
~~~~

<p>
\4) Remove colon from end of case statement:

    :$

<p>
\5) Remove return statement and leading whitespace:

    ^\s+return new string\[\]\s*

<p>
I ended up with a sequence of couplets looking similar to this one:

~~~~ {name="code" language="csharp"}
PermissionKey.SecurityParameterManagementAdd{"Security", "ParameterManagement", "Add"};
~~~~

Now the fun starts - lets walk through the process.

We want to convert the first couplet into a simple unit test fixture,
and record the process. This will be our macro - the instructions for
converting one couplet into one unit test. We can then play the macro
multiple times to convert all the others effortlessly.

Start by moving the cursor to the start of the line, before the 'P' of
PermissionKey. This is the start point of the macro, so for the macro to
be repeatable we must make sure that we finish recording the macro in
perfect position to run it again, i.e. before the 'P' of PermissionKey
for the next couplet (column 0 line 3). Hit Ctrl-Shift-R to start
recording.

It is important not to use the mouse when editing - stick to the
keyboard. It's also important not to record keystrokes that are too
specific to one bit of code. For instance, don't use the arrow keys to
move left and right character-by-character, because it won't work on
longer or shorter lines.

Instead, use the Home and End keys to jump to the start or end of the
line, and hold Ctrl whilst arrowing left or right to move a word at a
time instead of a character at a time (this is one of the areas where
vim's movement commands really differentiate it from wannabes like
Notepad++...but I digress). See the 'Detailed Instructions' section
below for more information.

<p>
Assume the original switch body is in a method called
'LookupEnumPermission'. The couplet should be edited to look like this
(without the linewrap...):

~~~~ {name="code" language="csharp"}
[Test]public void TestSecurityParameterManagementAdd(){    string[] result = LookupEnumPermission(            PermissionKey.SecurityParameterManagementAdd);    Assert.AreEqual("Security", result[0]);    Assert.AreEqual("ParameterManagement", result[1]);    Assert.AreEqual("Add", result[2]);}
~~~~

Make sure you finish by moving the cursor into position for the next
couplet, and hit Ctrl-Shift-R again to stop recording.

Now, hit Ctrl-Shift-P to play back the macro. If you've done everything
right, the next couplet should magically format itself into a unit test.
Hit Ctrl-Shift-P again, and the next couplet will change too. Under the
Macro menu, select 'Run a macro multiple times...' and you can enter a
fixed number of iterations, or just apply the macro over and over again
until the end of the file is reached.

Finally, you can copy the unit tests into a new or existing test
fixture, and you're done! In much less time (hopefully) and with fewer
errors than if the tests had been written one-by-one.

***Detailed Instructions:***

These are ley-by-key instructions in Notepad++, in case something in the
description above is unclear. Visual Studio should be similar. Vim will
be faster once you've learned how, but I'll assume if you use vim you're
already au fait with this sort of editing :-)

1.  Type [Test], and hit enter to start a new line.
2.  Type 'public void Test' and hit Enter.
3.  Type '{' and hit Enter, then Tab.
4.  Hold Ctrl and tap the right arrow twice to jump over a couple of
    words and place the cursor at the start of the word
    SecurityParameterManagementAdd, then hold Ctrl-Shift and right arrow
    again to select the word. Ctrl-C to copy, then arrow up two lines
    and paste it after the word 'Test' to create the full function name
    TestSecurityParameterManagementAdd. Type () for the empty parameter
    list.
5.  Arrow down two lines and hit Home to jump to the start of the line.
    Type 'string[] result = LookupEnumPermission(', then hit End to jump
    to the end of the line and type ');'.
6.  Arrow down one line, hit Home, then Tab. Type 'Assert.Equals(' then
    hit Delete to remove the '{'. Hold Ctrl and move right three times
    (to move the cursor just past the comma) and type 'result[0]);' and
    hit Enter.
7.  Repeat variations of step 7 a couple of times to convert the next
    two lines. Remember to use the correct indexes (result[1] and
    result[2]). Hit Enter after the last line and type '}' to close the
    function body.
8.  Arrow down one line and hit Home to place the cursor at the correct
    start position for the next couplet, and end the macro by hitting
    Ctrl-Shift-R again.

^[1]^I could have just done this in a new file in Visual Studio, but for
some reason I find VS intolerably slow at running macros once recorded.
So slow, in fact, that you can watch the cursor laboriously complete
each step - I wind up thinking it would have been quicker to do it
manually. That might just be something odd about my VS installation
though, as no-one else seems to think it's slow.
