#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import date
from itertools import chain, repeat, zip_longest
import os
from pathlib import Path
from typing import Sequence


def to_date(value: Sequence) -> date:
    """ A Jinja filter for converting an object to a date."""
    # Set 1 as the default value for missing variables
    year, month, day = chain(value, repeat(1, 3 - len(value)))
    return date(year, month, day)


def page_range(value: Sequence, current_page: int, interval: int = 3) -> range:
    """Return the range which is `interval` wide in which current_page lies."""
    end = len(value) + 1
    start_sequence = range(1, end, interval)  # 1, 4, 7, ...
    end_sequence = range(1 + interval, end, interval)  # 4, 7,...
    for start, end in zip_longest(start_sequence, end_sequence, fillvalue=end):
        if current_page in range(start, end):
            return range(start, end)


JINJA_FILTERS = {
    'zip': zip,
    'to_date': to_date,
    'page_range': page_range
}

AUTHOR = 'Ishaan Arora'
SITENAME = "pulsar17's blog"
SITEURL = os.environ.get('PELICAN_IS_LOCAL', 'https://pulsar17.me')

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
FEED_RSS = 'feed/index.xml'
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

YEAR_ARCHIVE_URL = 'archive/{date:%Y}'
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'

MONTH_ARCHIVE_URL = 'archive/{date:%Y}/{date:%m}'
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/{date:%m}/index.html'

AUTHOR_URL = 'authors/{slug}'
AUTHOR_SAVE_AS = 'authors/{slug}.html'


MAIN_NAVIGATION = ['categories', 'tags', 'archives']
DIRECT_TEMPLATES = ['index'] + MAIN_NAVIGATION


PATH = 'content'
STATIC_PATHS = ['images','js', 'logos', 'fonts', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

GITLAB_ID = GITHUB_ID = 'pulsar17'

DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

JS_FILE = 'main.js'
