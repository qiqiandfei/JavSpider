# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
from JavSpider.settings import USER_AGENT_LIST, DEFAULT_REQUEST_HEADERS
from readini import ReadConfig
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message

class JavspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JavspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        referer = request.url
        if referer:
            request.headers["referer"] = referer
        rand_use = random.choice(USER_AGENT_LIST)  # 这个USER_AGENT_LIST是从settings里面导入的
        if rand_use:
            request.headers.setdefault('User-Agent', rand_use)

        #删除默认
        defaulcookie = ''
        if 'existmag=all' in DEFAULT_REQUEST_HEADERS['cookie']:
            defaulcookie = DEFAULT_REQUEST_HEADERS['cookie'].replace(' existmag=all;', '')

        if 'existmag=mag' in DEFAULT_REQUEST_HEADERS['cookie']:
            defaulcookie = DEFAULT_REQUEST_HEADERS['cookie'].replace(' existmag=mag;', '')

        config = ReadConfig()
        #获取全部磁力
        if config.get_markconfig('crawlall') == 'yes':
            cookie = defaulcookie + " existmag=all;"
        #获取存在磁力
        else:
            cookie = defaulcookie + " existmag=mag;"
        request.headers['Cookie'] = cookie


class CustomRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        if response.status == 429:
            # 更长的随机延迟（10-30秒）
            retry_delay = random.uniform(10, 30)
            spider.logger.warning(f'Rate limited (429), retrying in {retry_delay:.2f}s...')
            
            # 自动降低请求优先级（数值越小优先级越低）
            request.priority = request.priority - 100 if hasattr(request, 'priority') else -100
            
            request.meta['retry_delay'] = retry_delay
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response
        return super().process_response(request, response, spider)