post_id: pg-wodehouse-method-of-refactoring
Author: Fortran IV
Date: 2008-03-23 18:28:07
Author_Email: noreply@blogger.com
Author_IP: None

Jacob:  An "edge condition" is when the behavior of an otherwise uniform
system changes as you approach its boundaries.

In physics, for instance, imagine a massive (non-rotating) flat disk with a
diameter of, say, the planet Jupiter.  Over most of the disk's surface you can
stand upright.  Due to the relative size of the disk to yourself, the effect
of gravity is effectively perpendicular to the disk's surface, because the
force of gravity falls off with the square of distance.  But as you walk
toward the edge of the disk, you begin to lean outward as the gravitational
effect becomes less uniform.

In computer graphics, you may have an edge condition if you attempt to draw a
line with one or both endpoints off the screen and out of the screen buffer.
Or think of operations such as noise reduction, smoothing, or resizing of an
image by comparing neighboring pixels; your code must allow for the edge
condition where a given pixel has NO neighbors on one or two sides.

John:  A co-worker once described to me another sort of "rooftop debugging"
technique he saw back in the seventies.  The programmers printed a hex dump of
machine memory at the time of a program failure (back before such a dump might
cover a few hundred acres), spread it on the lawn, then climbed up on the roof
and looked for visual patterns in the hex.  Pretty desperate.
