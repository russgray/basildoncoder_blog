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
DEFAULT_DATE = 'fs'

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
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.subscript': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# templates
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))

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

TWITTER_FEED = {
    'href': 'https://twitter.com/russgray',
    'data_widget_id': '519773559837573120',
    'data_chrome': 'nofooter noheader transparent',
    'data_tweet_limit': '3',
    'username': 'russgray'
}

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

FEATURED_POSTS = [
    'pg-wodehouse-method-of-refactoring',
    'marshalling-variable-length-array-from',
    'turbocharging-net-webservice-clients',
]

LANDING_PAGE_ABOUT = {
        'title': 'Java by day, .Net and python by night',
        'details': """

            <div itemscope itemtype="http://schema.org/Person">

                <p>My name is <span itemprop="name">Russell Gray</span>. I am <a
            href="https://github.com/russgray/" title="My Github profile"
            itemprop="url"><span itemprop="nickname">russgray</span></a> at Github and <a
            href="https://twitter.com/russgray/" title="My Twitter profile"
            itemprop="url">@russgray</a> at twitter.</p>

               <p>I work at <a href="https://www.patientsknowbest.com/" title="Patients Know Best"
            itemprop="affiliation">PKB</a>, a healthcare startup, as a
            backend developer focussing on performance, profiling, and new
            features.</p>

            </div>

       """}




