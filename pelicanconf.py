#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Russell Gray'
SITENAME = u'Basildon Coder'
SITEURL = 'http://localhost:8000'

PATH = 'content'
THEME = 'themes/elegant'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    )

# Social widget
SOCIAL = (
    ('Twitter', '@russgray'),
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['/opt/pelican-plugins']
PLUGINS = ['pelican_comments', 'render_math', 'tipue_search', 'sitemap', 'extract_toc']
ARTICLE_EXCLUDES = ['comments', 'pages']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'subscript', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

SOCIAL = (
        ('Twitter', 'http://twitter.com/russgray'),
        ('Github', 'http://github.com/russgray'),
        ('Email', 'mailto:russgray@gmail.com'),
          )

# Landing Page
PROJECTS = [{
                'name': 'Tagwager',
                'url': 'http://www.tagwager.com/',
                'description': 'Automated betting analytics'
            },
            {
                'name': 'Balanced News',
                'url': 'https://www.balancednews.co.uk/',
                'description': 'Your unbiased UK news source'
            },
            {
                'name': 'Essex Backups',
                'url': 'https://www.essexbackup.co.uk/',
                'description': 'Zero-tech backup service'
            },
        ]
LANDING_PAGE_ABOUT = {
        'title': 'Software developer, tinkerer, etc',
        'details': """

        <div itemscope itemtype="http://schema.org/Person">

            <p>My name is <span itemprop="name">Talha Mansoor</span>. I am <a
        href="https://github.com/talha131/" title="My Github profile"
        itemprop="url"><span itemprop="nickname">talha131</span></a> at Github and <a
        href="https://twitter.com/talham_/" title="My Twitter profile"
        itemprop="url">@talham_</a> at twitter. You can also reach me via <a
        href="mailto:talha131@gmail.com" title="My email address"
        itemprop="email">email</a>.</p>

           <p>I work on <a href="http://jumpdesktop.com/" title="Jump Desktop"
        itemprop="affiliation">Jump Desktop</a> which is a remote desktop application
        for iOS, OSX and Android. I play a broad role there - which includes research,
        product design, engineering and deployment. I also lend a hand in user
        support.</p>

           <p>I try to contribute to society by striving to create great software
        products that make people's lives easier. I believe software is the most
        effective way to touch others' lives in our day and time.</p>

            <p>I mostly work in C, C++ and Objective-C on OSX and Linux, I also
        dabble in Python, Vim-L and JavaScript. I do not pigeonhole myself to specific
        languages or frameworks. A good developer is receptive and has the ability to
        learn new technologies. I also often contribute to open source projects and
        beta test startup products. </p>

            <p>Besides programming, I <a href="https://www.fitocracy.com/profile
        /Andrew-Dufresne/" title="My Fitocracy profile" itemprop="url">exercise</a>
        and <a href="http://www.goodreads.com/talha131" title="My GoodReads profile"
        itemprop="url">read books</a> regularly. To be a stronger and better version
        of myself!</p>

            <p>English is my second language. I am also learning <a
        href="http://www.duolingo.com/talha131" title="My Duolingo profile"
        itemprop="url">German from Duolingo</a>.</p>

        </div>

       """}
