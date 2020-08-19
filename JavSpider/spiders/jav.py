# -*- coding: utf-8 -*-
"""
 * Create by: yufei
 * Date: 2020/7/7
 * Time: 10:50
 * Name: JAV磁力抓取脚本
 * Porpuse: 根据车牌、老师抓取'https://javbus.com'的磁力链接
 * Copyright © 2020年 Fei. All rights reserved.
"""
import scrapy
from JavSpider.items import JavspiderItem
from readini import ReadConfig


class JavSpider(scrapy.Spider):
    name = 'jav'
    crawlrule = ''
    conditions = []
    mosaic = ''
    allowed_domains = []
    def start_requests(self):
        #读取配置
        config = ReadConfig()
        self.allowed_domains.append(config.get_markconfig('domain'))
        self.crawlrule = config.get_markconfig('crawlrule')
        self.mosaic = config.get_markconfig('mosaic')
        conditilist = config.get_markconfig('condition').split(',')
        for item in conditilist:
            if item is not None or item != '':
                self.conditions.append(item)

        #欧美影片只支持清晰度抓取
        if self.allowed_domains == 'https://www.javbus.one':
            self.crawlrule = '清晰度'

        #爬爬爬
        for condition in self.conditions:
            url = self.allowed_domains[0] + '/search/{}&type=&parent=ce'.format(condition)
            yield scrapy.Request(url=url, meta={'condition': condition}, callback=self.parse)

    def parse(self, response):
        #日本影片抓取
        if 'javbus.one' not in self.allowed_domains[0]:
            qbmovie = response.xpath("/html/body/div[4]/div/div[4]/ul/li[1]/a/text()[2]").extract()[0].strip()[:-1].strip()
            bbmovie = response.xpath("/html/body/div[4]/div/div[4]/ul/li[2]/a/text()[2]").extract()[0].strip()[:-1].strip()

            # 有码影片
            if self.mosaic == 'yes' or self.mosaic == 'all':
                if int(qbmovie) > 0:
                    #查询页数
                    pagelist = response.xpath("//ul[@class='pagination pagination-lg']//@href").extract()
                    if len(pagelist) == 0:
                        url = response.url
                        yield scrapy.Request(url=url, meta={"type": '骑兵', 'page': 1, 'condition': response.meta['condition']}, callback=self.parse_movie, dont_filter=True)
                    else:
                        url = self.allowed_domains[0] + '/search/' + response.meta['condition'] + '/1'
                        yield scrapy.Request(url=url, meta={"type": '骑兵', 'page': 1, 'condition': response.meta['condition']}, callback=self.parse_movie, dont_filter=True)

            # 无码影片
            if self.mosaic == 'no' or self.mosaic == 'all':
                if int(bbmovie) > 0:
                    url = response.xpath("/html/body/div[4]/div/div[4]/ul/li[2]/a/@href").extract_first()
                    yield scrapy.Request(url=url, meta={"type": '步兵', 'page': 1, 'condition': response.meta['condition']}, callback=self.parse_uncensored, dont_filter=True)
        else:
            #欧美影片抓取
            url = self.allowed_domains[0] + '/search/' + response.meta['condition'] + '/1'
            yield scrapy.Request(url=url, meta={"type": '欧美', 'page': 1, 'condition': response.meta['condition']},callback=self.parse_movie, dont_filter=True)

    #无码影片抓取
    def parse_uncensored(self, response):
        pagelist = response.xpath("//ul[@class='pagination pagination-lg']//@href").extract()
        if len(pagelist) == 0:
            url = response.url
            yield scrapy.Request(url=url, meta={"type": '步兵', 'page': 1, 'condition': response.meta['condition']}, callback=self.parse_movie, dont_filter=True)
        else:
            url = self.allowed_domains[0] + '/uncensored/search/' + response.meta['condition'] + '/1'
            yield scrapy.Request(url=url, meta={"type": '步兵', 'page': 1, 'condition': response.meta['condition']}, callback=self.parse_movie, dont_filter=True)


    def parse_movie(self, response):
        next = response.xpath("//*[@id='next']").extract()
        curpage = response.meta['page']
        condition = response.meta['condition']
        #最后一页
        if len(next) == 0:
            movielist = response.xpath("//div[@id='waterfall']//@href").extract()
            type = response.meta["type"]
            for movieurl in movielist:
                yield scrapy.Request(url=movieurl, meta={"type": type}, callback=self.parse_magnet, dont_filter=True)
        else:
            #先抓本页，本页抓完递归抓下页
            movielist = response.xpath("//div[@id='waterfall']//@href").extract()
            type = response.meta["type"]
            for movieurl in movielist:
                yield scrapy.Request(url=movieurl, meta={"type": type}, callback=self.parse_magnet, dont_filter=True)
            if type == '骑兵':
                url = self.allowed_domains[0] + '/search/' + condition + '/' + str(curpage + 1)
            if type == '步兵':
                url = self.allowed_domains[0] + '/uncensored/search/' + condition + '/' + str(curpage + 1)
            yield scrapy.Request(url=url, meta={"type": type, 'page': curpage + 1, 'condition': condition}, callback=self.parse_movie, dont_filter=True)

    def parse_magnet(self, response):
        #拼接请求参数用于获取磁力链接
        param = response.xpath("/html/body/script[3]/text()").extract()[0]
        param = param.replace(' ', '')
        param = param.replace('\r\n\tvar', '')
        param = param.replace('\r\n', '')
        param = param.replace(';', '&')
        param = param.replace("'", '')
        #页面反爬无法获取磁力信息，磁力通过ajax请求获取
        magneturl = self.allowed_domains[0] + '/ajax/uncledatoolsbyajax.php?' + param + 'floor=827'
        date = response.xpath("/html/body/div[5]/div[1]/div[2]/p[2]/text()").extract_first()
        title = response.xpath("/html/body/div[5]/h3/text()").extract_first()
        coverimg = response.xpath("/html/body/div[5]/div[1]/div[1]/a/img//@src").extract_first()
        type = response.meta["type"]
        yield scrapy.Request(url=magneturl, meta={"type": type, 'date': date, 'title': title, 'coverimg': coverimg}, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        jav = JavspiderItem()
        jav['title'] = response.meta['title'].strip()
        jav['type'] = response.meta['type']
        jav['date'] = response.meta['date'].strip()
        jav['coverimg'] = response.meta['coverimg']
        #判断磁力链接状态
        magnetstate = response.xpath("//tr//td[1]/text()").extract_first()
        if 'There is no magnet link for this video at the moment, please wait for others to share it!' == magnetstate:
            return
        elif 'The following magnet link is Pending Review!' == magnetstate:
            if self.crawlrule == '清晰度':
                sizelist = response.xpath("//tr[2]//td[2]//a/text()").extract()
                # 找到清晰度最高的
                index, newlist = self.getlargeone(sizelist)
                href = response.xpath("//tr[2]//td[2]//a//@href").extract()[index]
                jav['magnet'] = href
                jav['size'] = newlist[index]
                # 判断是否有字幕
                subtitlelist = response.xpath("//tr[2]//td[1]").extract()
                if self.hassubtitle(subtitlelist, index):
                    jav['subtitle'] = '是'
                else:
                    jav['subtitle'] = '否'

            if self.crawlrule == '字幕':
                subtitlelist = response.xpath("//tr[2]//td[1]").extract()
                sizelist = response.xpath("//tr[2]//td[2]//a/text()").extract()
                index = self.getsubtitle(subtitlelist)
                # 没有带字幕的视频按清晰度查找
                if index == -1:
                    # 找到清晰度最高的
                    index, newlist = self.getlargeone(sizelist)
                    href = response.xpath("//tr[2]//td[2]//a//@href").extract()[index]
                    jav['magnet'] = href
                    jav['size'] = newlist[index]
                    jav['subtitle'] = '否'
                else:
                    # 找到带字幕的
                    newlist = self.sizeformat(sizelist)
                    href = response.xpath("//tr[2]//td[2]//a//@href").extract()[index]
                    jav['magnet'] = href
                    jav['size'] = newlist[index]
                    jav['subtitle'] = '是'
        else:
            if self.crawlrule == '清晰度':
                sizelist = response.xpath("//tr//td[2]//a/text()").extract()
                #找到清晰度最高的
                index, newlist = self.getlargeone(sizelist)
                href = response.xpath("//tr//td[2]//a//@href").extract()[index]
                jav['magnet'] = href
                jav['size'] = newlist[index]
                #判断是否有字幕
                subtitlelist = response.xpath("//tr//td[1]").extract()
                if self.hassubtitle(subtitlelist, index):
                    jav['subtitle'] = '是'
                else:
                    jav['subtitle'] = '否'

            if self.crawlrule == '字幕':
                subtitlelist = response.xpath("//tr//td[1]").extract()
                sizelist = response.xpath("//tr//td[2]//a/text()").extract()
                index = self.getsubtitle(subtitlelist)
                #没有带字幕的视频按清晰度查找
                if index == -1:
                    # 找到清晰度最高的
                    index, newlist = self.getlargeone(sizelist)
                    href = response.xpath("//tr//td[2]//a//@href").extract()[index]
                    jav['magnet'] = href
                    jav['size'] = newlist[index]
                    jav['subtitle'] = '否'
                else:
                    # 找到带字幕的
                    newlist = self.sizeformat(sizelist)
                    href = response.xpath("//tr//td[2]//a//@href").extract()[index]
                    jav['magnet'] = href
                    jav['size'] = newlist[index]
                    jav['subtitle'] = '是'
        yield jav

    def hassubtitle(self, subtitlelist, index):
        if 'Subtitles">SUB</a>' in subtitlelist[index]:
            return True
        else:
            return False
    """
    找到清晰度最高的磁力
    """
    def getlargeone(self, sizelist):
        max = []
        index = -1
        newlist = self.sizeformat(sizelist)

        for i in range(0, len(newlist)):
            if len(max) == 0:
                max.append(newlist[i])
                index = i
            else:
                cur = 0.0
                if newlist[i][len(newlist[i]) - 2:] == 'GB':
                    cur = float(newlist[i][0:-2]) * 1024
                if newlist[i][len(newlist[i]) - 2:] == 'MB':
                    cur = float(newlist[i][0:-2])
                last = 0.0
                if max[0][len(max[0]) - 2:] == 'GB':
                    last = float(max[0][0:-2]) * 1024
                if max[0][len(max[0]) - 2:] == 'MB':
                    last = float(max[0][0:-2])
                if cur > last:
                    max.clear()
                    max.append(newlist[i])
                    index = i
        return index, newlist

    """
    格式化文件大小列表
    """
    def sizeformat(self, sizelist):
        newlist = []
        for item in sizelist:
            tmp = item.replace('/r/n', '')
            tmp = tmp.replace('\t', '')
            tmp = tmp.strip()
            newlist.append(tmp)
        return newlist

    """
    找到带字幕的序号
    """
    def getsubtitle(self, subtitlelist):
        index = -1
        #先找高清 + 字幕
        for i in range(0, len(subtitlelist)):
            if 'HD Videos">HD</a>' in subtitlelist[i] and 'Subtitles">SUB</a>' in subtitlelist[i]:
                index = i
                return index

        #找不到高清 + 字幕找字幕
        if index == -1:
            for i in range(0, len(subtitlelist)):
                if 'Subtitles">SUB</a>' in subtitlelist[i]:
                    index = i
                    return index
        return index


