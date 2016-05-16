Title: In Defence Of Coffeescript
Author: Russell Gray
Slug: in-defence-of-coffeescript
Tags: coding, javascript, coffeescript, react, gulp
Status: draft

It seems quite trendy these days to bash coffeescript as an unnecessary abstraction, proposing instead to use javascript directly. I would agree that you don't really want to be transpiling coffeescript in the browser, but assuming I'm using any sort of build pipeline I much prefer it.

A couple of weeks back I had an idea for a toy site that would actually benefit from being a single-page app (SPA) with no real backend requirement, so I decided to use it as an opportunity to ship something using React.js and GulpJS. These are two of the more talked-about front-end releases of 2014 (and ye gods, do people ever *talk* about fashionable new front-end code!)

GulpJS is the latest build system to be built in node, and many prefer it to the so-last-year Grunt. It allows you to write build tasks (including minification, concatenation etc) as pipelines, with callbacks everywhere you look (this *is* node, after all).

It is totally possible to write your gulpfile in coffeescript with a simple bootstrapper in gulpfile.js. I have to say I prefer this:

    :::coffeescript
    gulp.task 'js:minify', ['browserify'], ->
        gulp.src './output/react-monitorbox.js'
            .pipe plumber()
            .pipe uglify()
            .pipe rename suffix:'.min'
            .pipe gulp.dest './dist'

to this:

    :::javascript
    gulp.task('js:minify', ['browserify'], function() {
        return gulp.src('./output/react-monitorbox.js')
            .pipe(plumber())
            .pipe(uglify())
            .pipe(rename({ suffix: '.min' }))
            .pipe(gulp.dest('./dist'));
    });

React.js is Facebook's lib for serious front-end work and is much more lightweight, conceptually, than Google's AngularJS. Slightly controversially, it uses a template language called JSX to allow you to write markup in your script, which gets transpiled to raw javascript API calls. Unsurprisingly the raw JS is a bit ugly, which is why Facebook hide it behind a DSL.

    :::javascript
    var CommentBox = React.createClass({
        render: function() {
            return (
                <div className="commentBox">
                Hello, world! I am a CommentBox.
                </div>
            );
        }
    });

    :::coffeescript
    CommentBox = React.createClass
        render: ->
            R.div className:"commentBox",
                'Hello, world! I am a CommentBox.'

http://neugierig.org/software/blog/2014/02/react-jsx-coffeescript.html