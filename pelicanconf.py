#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pedro Vidigal'
SITENAME = "Pedro Vidigal's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/robots.txt': {'path': 'robots.txt'},
                       }

TYPOGRIFY = True

PLUGIN_PATHS = ['/home/vidigalp/Code/pelican-addon-clones/pelican-plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

THEME = '/home/vidigalp/Code/pelican-addon-clones/pelican-themes/pelican-bootstrap3'
STATIC_PATHS = ['img', 'static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'