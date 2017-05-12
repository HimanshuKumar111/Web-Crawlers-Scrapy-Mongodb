# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DatainfoItem(scrapy.Item):
	title = scrapy.Field()
	datasets = scrapy.Field()
	visual_access= scrapy.Field()
	last_updated = scrapy.Field()
	views = scrapy.Field()
	downloads = scrapy.Field()
	ministry = scrapy.Field()

