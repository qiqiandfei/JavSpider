# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import os
#from JavSpider.settings import USER_CONFIG
from readini import ReadConfig

class JavspiderPipeline(object):
    def __init__(self):
        # condition = USER_CONFIG['condition'][0]
        # crawlrule = USER_CONFIG['crawlrule']
        #
        # mosaic = ''
        # if USER_CONFIG['mosaic'] == 'yes':
        #     mosaic = '骑兵'
        # elif USER_CONFIG['mosaic'] == 'no':
        #     mosaic = '步兵'
        # elif USER_CONFIG['mosaic'] == 'all':
        #     mosaic = '全部'
        #
        # if len(USER_CONFIG['condition']) > 1:
        #     info = condition + '..._' + crawlrule + '_' + mosaic + '_info.json'
        #     magnet = condition + '..._' + crawlrule + '_' + mosaic + '_magnet.txt'
        # else:
        #     info = condition + '_' + crawlrule + '_' + mosaic + '_info.json'
        #     magnet = condition + '_' + crawlrule + '_' + mosaic + '_magnet.txt'
        config = ReadConfig()
        conditions = []
        crawlrule = config.get_markconfig('crawlrule')

        mosaic = ''
        if config.get_markconfig('mosaic') == 'yes':
            mosaic = '骑兵'
        elif config.get_markconfig('mosaic') == 'no':
            mosaic = '步兵'
        elif config.get_markconfig('mosaic') == 'all':
            mosaic = '全部'

        conditilist = config.get_markconfig('condition').split(',')

        for item in conditilist:
            if item is not None or item != '':
                conditions.append(item)

        if len(conditions) > 1:
            info = conditions[0] + '..._' + crawlrule + '_' + mosaic + '_info.json'
            magnet = conditions[0] + '..._' + crawlrule + '_' + mosaic + '_magnet.txt'
        elif len(conditions) == 1:
            info = conditions[0] + '_' + crawlrule + '_' + mosaic + '_info.json'
            magnet = conditions[0] + '_' + crawlrule + '_' + mosaic + '_magnet.txt'
        else:
            info = 'JavALl_' + crawlrule + '_' + mosaic + '_info.json'
            magnet = 'JavALl_' + crawlrule + '_' + mosaic + '_magnet.txt'

        #创建结果文件夹
        if not os.path.exists('CrawlResult'):
            os.mkdir('CrawlResult')

        self.file = codecs.open('CrawlResult/' + info, 'w', encoding='utf-8')
        self.txt = codecs.open('CrawlResult/' + magnet, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        dic = json.loads(line)
        self.txt.write(dic['magnet'] + '\r\n')
        return item

    def spider_closed(self, spider):
        self.txt.close()
        self.file.close()
