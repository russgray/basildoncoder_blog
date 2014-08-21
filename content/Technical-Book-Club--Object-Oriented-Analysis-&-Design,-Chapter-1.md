Title: Technical Book Club: Object Oriented Analysis & Design, Chapter 1
Date: 2008-01-27 23:31
Author: Russell Gray
Slug: Technical-Book-Club-Object-Oriented-Analysis-Design-Chapter-1
Tags: book club, software engineering

![image](http://ecx.images-amazon.com/images/I/51-uo4HUPCL._AA240_.jpg)So, as
[previously mentioned]({filename}/Technical-Book-Club.md), we'll start with
the basics. This material is probably very familiar to most coders with even a
small amount of experience, but it never hurts to refresh the fundamentals.
You may even find that there's some material that seems so obvious you don't
even actively think about it any more - which is good if it has become habit,
but may be bad if you've grown complacent in certain areas.

The overarching theme of the first chapter is **complexity**. Complexity
is the enemy of the software developer, and it is vital to understand
this fact. If you don't identify complexity as the enemy, you will find
it harder to remain vigilant against it.

Anyone who has worked as a developer for more than a year or two will
almost certainly have exposure to the problems caused by complexity, but
quite often complexity itself will not be pinpointed as the root cause.
It may be a case of not seeing the wood for the trees - when trying to
understand a system it's very easy to get bogged down wondering why some
particular section of code does things a certain way, and not see the
problems with the big picture. Of course, since complexity obscures the
big picture, this is common and self-perpetuating.

Object-oriented design, then, is a tool for managing complexity. Of
course, it is many other things too, but this is one of the
fundamentals. In particular, OOD is a natural way to represent
**hierarchies**, and hierarchies are the primary tool Booch presents for
making complexity manageable. A number of examples from nature are
provided; for example, you can view a plant simply as a plant, or as a
collection of structures (leaves, stem, roots).

![image]({filename}/images/flower.jpg)Importantly, the
overall hierarchical view of a plant can be broken down into many
interacting sub-hierarchies, each of which may be considered in terms of
its own structure and its **interactions**. This is an example of
**decomposition**. If you want to study roots in detail, you can study
the branch roots, the root apex, and the root cap - and break that down
further if you like to consider roots as a collection of cells. To study
roots in this sort of detail, however, you do not have to go to the same
lengths with leaves and stems - it is enough to understand the
interactions between the higher-level components.

Complexity, therefore, is more manageable if it is divided into
interacting components, each of which can be further divided into
interacting subcomponents. At different levels of abstraction there are
clear boundaries - it shouldn't be necessary to understand the epidermis
of a leaf to examine a root, and likewise the study of a leaf should not
need to consider the role of the root apex. This is known as
**separation of concerns**, and allows you to ignore the parts of the
system that you are not interested in at the time.

In software, these principles are captured by OOD. Broadly, hierarchies
can be modelled with inheritance, components can be modelled with
modules, intercomponent interactions can be modelled with interfaces and
method calls, and intracomponent interactions can be modelled with
aggregation. These interactions are key, as they form part of the
'value' of a system - in layman's terms, the whole is greater than the
sum of its parts.

![image]({filename}/images/jetengine.jpg)Inheritance and
aggregation are, respectively, 'is-a' and 'part-of' relationships. In
both cases, these represent separate but overlapping hierarchies.
Booch's example is that of an aeroplane. An aeroplane can be thought of
as an aggregation of systems - propulsion, flight control, etc. Each of
those can potentially be modelled as specilaised types too - for
instance a jet engine is a particular type of propulsion, and a turbofan
engine is a particular type of jet engine.

In OO terms, the 'is-a' relationships are expressed as **class
structures** utilising inheritance, and 'part-of' relationships are
expressed as **object structures** utilising aggregation.

**Relative primitives** are an interesting concept, and refer as much as
anything to the benefit of having a sensible and appropriate vocabulary
at each level of abstraction. With plants, for instance, if you are
working at the cellular level your primitives are nuclei, chloroplasts
etc. If, however, you are at the top level your primitives should be
leaves and stems - something is wrong if you are concerning yourself
with the nucleus of a cell at this level of abstraction. Relative
primitives are a natural consequence of hierarchies and decomposition,
if your hierarchies are sane.

Even with all these tools for managing complexity at our disposal, it is
still extraordinarily hard - if not nigh-on impossible - to construct a
large complex system in one fell swoop. Booch identifies that a key
characteristic of successful complex systems is that they evolve from
simpler systems, whilst always being useful during that evolution - they
have **stable intermediate forms**.

Contemporary development processes, such as agile development,
explicitly recognise this with the mantra of 'deliver early, deliver
often'. The idea is that functionality should be delivered iteratively,
with each iteration being functional and testable. This is in contrast
to more traditional waterfall methodologies, which are notoriously
associated with failed projects, often due to attempting to design a
large complex system up-front and develop it all at once.

In summary, then, Booch argues that the characteristics of a manageable
complex system are as follows:

- Hierarchic
- Uses relative primitives
- Has robust separation of concerns
- Has stable intermediate forms

It is important to note in passing that, since OOA&D is an unashamed
champion of object-orientation as a mechanism for managing complexity,
OO is by no means the only approach - functional and procedural
languages have their own techniques, and in some cases may be more
suitable, depending on the problem to be solved. Even so, many of these
principles are common and are useful things to bear in mind when
designing a system.

Next week we look at chapter 2, which covers the object model in greater
detail.
