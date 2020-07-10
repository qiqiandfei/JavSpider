# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JavspiderItem(scrapy.Item):
    number = scrapy.Field()
    actor = scrapy.Field()
    title = scrapy.Field()  #标题（车牌 + 老师 + 片名）
    magnet = scrapy.Field() #磁力链接
    size = scrapy.Field()   #文件大小
    date = scrapy.Field()   #发布日期
    type = scrapy.Field()   #骑兵/步兵
    subtitle = scrapy.Field()   #是否有字幕

