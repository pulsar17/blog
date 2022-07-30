#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
from pathlib import Path

AUTHOR = 'Ishaan Arora'
SITENAME = "pulsar17's blog"
SITEURL = os.environ.get('PELICAN_IS_LOCAL', 'https://pulsar17.me')

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Expect apricot to be on the same level in the filesystem as this module
THEME = str(Path(".").resolve() / "apricot")
FAVICON = "logos/favicon.ico"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Clean URLs

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}.html'
CATEGORIES_URL = 'categories'  # Custom
CATEGORIES_SAVE_AS = 'categories/index.html'

TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_SAVE_AS = 'tags/index.html'

YEAR_ARCHIVE_URL = '/archive/{date:%Y}'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'

MONTH_ARCHIVE_URL = '/archive/{date:%Y}/{date:%m}'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'

# Create a listing of posts with each category or tag in the categories and tags folders (respectively)

MAIN_NAVIGATION = ['categories', 'tags', 'archives']
DIRECT_TEMPLATES = ['index'] + MAIN_NAVIGATION

# Generate an index.html each for the categories and tags folders listing all the categories and all the tags

PATH = 'content'
STATIC_PATHS = ['images', 'logos', 'fonts', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

GITLAB_ID = GITHUB_ID = 'pulsar17'
