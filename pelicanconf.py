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

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True

PLUGIN_PATHS = ['/opt/pelican-plugins']
PLUGINS = ['pelican_comments', 'render_math', 'tipue_search', 'sitemap', 'extract_toc', 'neighbors']
ARTICLE_EXCLUDES = ['comments', 'pages']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'subscript', 'toc']

# templates
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

# additional static files/directories
STATIC_PATHS = ['theme/images', 'images', 'extra/robots.txt', 'extra/Russell-Gray-CV.pdf']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    }

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
        ('LinkedIn', 'http://uk.linkedin.com/in/russgray/'),
        ('Email', 'mailto:russgray@gmail.com'),
          )

GOOGLE_PLUS_PROFILE_URL = 'https://plus.google.com/u/0/102559471807447493728'

# Landing Page
PROJECTS = [{
                'name': 'Tagwager',
                'url': 'http://www.tagwager.com/',
                'description': 'Automated betting analytics'
            },
            {
                'name': 'Balanced News',
                'url': 'http://www.balancednews.co.uk/',
                'description': 'Your unbiased UK news source'
            },
            {
                'name': 'Essex Backups',
                'url': 'http://www.essexbackup.co.uk/',
                'description': 'Zero-tech backup service'
            },
        ]

LANDING_PAGE_ABOUT = {
        'title': '.Net by day, python come nightfall',
        'details': """

            <div itemscope itemtype="http://schema.org/Person">

                <p>My name is <span itemprop="name">Russell Gray</span>. I am <a
            href="https://github.com/russgray/" title="My Github profile"
            itemprop="url"><span itemprop="nickname">russgray</span></a> at Github and <a
            href="https://twitter.com/russgray/" title="My Twitter profile"
            itemprop="url">@russgray</a> at twitter.</p>

               <p>I work at <a href="http://www.livedrive.com/" title="Livedrive Internet"
            itemprop="affiliation">Livedrive</a>, on online cloud storage provider, as a
            backend developer focussing on performance, profiling, and writing new
            features.</p>

            </div>

       """}




