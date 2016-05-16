Title: 3-Way Merge In Vim
Date: 2014-10-30T14:20:21
Author: Russell Gray
Slug: 3-way-merge-in-vim
Tags: software engineering, vim

I have a nasty habit of forgetting certain commands when using vim to handle a
3-way merge, since the navigation is a bit non-standard. So, this is my (very
quick) reference.

Window layout shows the merged file at the bottom, the base (pre-conflict)
file top-middle, and the diverging diffs either side.

Cursor should be in the merged file which can be reached with standard window
navigation (e.g. `Ctrl-W j`).

    Previous conflict	[c
    Next conflict     	]c

Then, to resolve a conflict, use the `diffg` command to select a winner.

    Choose local  		:diffg LO
    Choose remote		:diffg RE
    Choose base   		:diffg BA

Choosing base effectively reverts both diffs. If the conflict is too complex
to fix by pulling a block, just rewrite as necessary in the merged file.

More info [here][1]

[1]: http://www.rosipov.com/blog/use-vimdiff-as-git-mergetool/
