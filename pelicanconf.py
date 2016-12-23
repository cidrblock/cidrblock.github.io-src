#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bradley A. Thornton'
SITENAME = u'network | automation'
SITEURL = ''

PATH = 'content'
THEME = 'themes/pelican-alchemy/alchemy'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('[drawthe.net]', 'http://drawthe.net/'),
          ('[#networktocode]', 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwiKscj5lYPRAhUT4GMKHdAsBM4QFgghMAE&url=https%3A%2F%2Ftwitter.com%2Fjedelman8%2Fstatus%2F663808419783045120&usg=AFQjCNGWhcMLiY_-O6QZwG82IxyIMHqXoA'),
          ('[comments/issues]', 'https://github.com/cidrblock/cidrblock.github.io-src/issues'),
          ('[netdevops resources]', 'network-automation-and-devops-resources.html')
        )
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

OUTPUT_RETENTION = [".git"]
