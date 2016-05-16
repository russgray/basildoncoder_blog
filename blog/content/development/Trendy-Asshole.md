Title: Trendy Asshole
Author: Russell Gray
Slug: trendy-asshole
Tags: coding, patterns
Status: draft

This is an opinionated tutorial on setting up a front-end web development environment.

I developed monitor-match as a simple site to try out some of the latest webdev hotness and establish for myself a 'preferred' stack for hobby projects (I mostly do backend performance work at my day job). This site has no backend at all - the dataset it works with is small enough that it can just be kept in code and downloaded in full by the browser.

The goal of monitor-match is simply to suggest good secondary monitors based on the calculated DPI of your primary monitor (the idea being that text will render at the same size on both, making it feel seamless to switch from one to the other). There are a few DPI calculators out there already, and some even allow comparisons, but none are very streamlined for what I want to do.

After reading around the subject for some time, I selected the following tools for my stack:

* **Vagrant** - I'll be using a Linux VM for creating the environment and running the build pipeline. Actual code editing can then be done on any host OS and editor - I'll mostly be using Sublime on Windows, switching to OSX if I'm on my laptop.
* **GulpJS** - selecting this kinda sets the tone for everything else. It means node and npm become the path of least resistance for getting dependencies.
* **Coffeescript** - gets a lot of hate for some reason. Fuck you, I like it.
* **SASS/Bourbon/Bitters/Neat/Refills** - like most backend devs, I have the aesthetic sense of a dung beetle. Using handy pre-baked kits like this gives me modern, standard, pretty CSS at the expense of looking a little...undistinguished. Still, at least it won't be another default bootstrap site, eh?
* **Handlebars** - rendered server-side, so I can pass some build-time parameters into my markup.
* **Bower** - for when npm gets boring.
* **React.js** - philosophically I prefer this to AngularJS. Simple, fast, and I like the one-way binding and readonly props, and I don't have to learn all the weird Angular vocabulary. Plus, no 2.0 debacle (yet). I won't be using the JSX markup though.
* **Jasmine** - yes, testing. Mmm, testing.

Quite the list there. With the wonders of modern development, this means I'll be pulling in half a gig of VM and about 70MB of libs to build a static site that will be less than 100KB minified. Hooray!
# Fair Warning
I've been writing software for 20 years, but I only really do front-end work for amusement. This tutorial is written from the perspective of someone who knows how to code, but isn't current with modern webdev. If you're a total newbie to coding, this may not be the tutorial for you.
# The Environment
Create a new directory. Run `git init`. Then run `vagrant init <preferred-distro>`. I'm using Ubuntu Trusty, which has implications for installing node. If you use something else, tweak the bootstrap script (below) as appropriate. When it completes, type `vagrant ssh` and then switch to the `/vagrant` directory, and you're all set.
# The Model
Create a `src` directory and a file called `monitor.coffee`. This will contain our basic monitor class and initialise the search corpus. We will want the following data:

* Resolution
* Diagonal screen size in inches
* DPI (calculated if necessary)
* Some metadata - a photo, description, Amazon link etc)

We'll suggest a specific monitor at each size though obviously any monitor at the same spec will match.

Here's the initial code:

	:::coffeescript
    class Monitor
        constructor: (@x, @y, @diag, @dpi=null, @name='', @uri='', @img='') ->
            @dpi = round_number(Math.sqrt(@x**2 + @y**2) / @diag) if not @dpi

If no DPI is provided, it is a simple calculation to work it out.