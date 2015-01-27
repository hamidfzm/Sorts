__author__ = 'hamid'
# -*- coding: utf-8 -*-

# python import
import os
from datetime import datetime


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass


    LANGUAGES = {
        'en': 'English',
        'fa': u'فارسی'
    }

    INSTALLED_BLUEPRINTS = ['main', 'api']

    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'UTC+03:30'

    SITE_TITLE = u'Sort Algorithms Comparisons'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
