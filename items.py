# -*- coding: utf-8 -*-

import scrapy

class BookItem(scrapy.Item):
    """
    Définition des champs pour les livres.
    """
    title = scrapy.Field()
    author = scrapy.Field()
