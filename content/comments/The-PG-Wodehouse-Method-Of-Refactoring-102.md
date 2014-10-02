post_id: pg-wodehouse-method-of-refactoring
Author: Anomalizer
Date: 2008-03-23 17:40:53
Author_Email: noreply@blogger.com
Author_IP: None

Identation is the key. A lot of people around me feel a moral obligation to
use an entirely different indentation scheme for every 10 lines and wonder why
I go ballistic when I see mixed schemes. I no longer argue over which scheme
is better; just use the same scheme throughout a project.

The next thing is to start collapsing statements based on the nesting level. I
start off with all blocks closed, and then do a hybrid of BFS and DFS of
sorts: indentify all blocks at level 'n', then pick the first of those and now
identify all of its children, then pick the first child and so on.
