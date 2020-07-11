# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import os
from JavSpider.settings import USER_CONFIG

class JavspiderPipeline(object):
    def __init__(self):
        
        condition = USER_CONFIG['condition'][0]
        crawlrule = USER_CONFIG['crawlrule']
        
        if len(USER_CONFIG['condition']) > 1:
            info = condition + '..._' + crawlrule + '_info.json'
            magnet = condition + '..._' + crawlrule + '_magnet.txt'
        else:
            info = condition + '_' + crawlrule + '_info.json'
            magnet = condition + '_' + crawlrule + '_magnet.txt'
        
        #创建结果文件夹
        if not os.path.exists('CrawlResult'):
            os.mkdir('CrawlResult')
            
        self.file = codecs.open('CrawlResult/' + info, 'w', encoding='utf-8')
        self.txt = codecs.open('CrawlResult/' + magnet, 'w', encoding='utf-8')
        self.splitline = 0

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        dic = json.loads(line)
        self.txt.write(dic['magnet'] + '\r\n')
        return item

    def spider_closed(self, spider):
        self.txt.close()
        self.file.close()
