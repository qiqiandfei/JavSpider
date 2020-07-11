# -*- coding: utf-8 -*-

# Scrapy settings for JavSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'JavSpider'

SPIDER_MODULES = ['JavSpider.spiders']
NEWSPIDER_MODULE = 'JavSpider.spiders'

#用户配置按需修改
USER_CONFIG = {

    # 设置主域名javbus主站需要fq，没有梯子的请填写放屏蔽地址例如：https://www.seedmm.cam
    # 防屏蔽地址不保证永久有效，失效需更换
    # 欧美影片域名填写'https://www.javbus.one'
    'domain': ['https://www.javbus.com'],
    #'domain': ['https://www.javbus.one'],

    # 过滤条件输入女优姓名，或者番号，支持混合输入，支持模糊输入，多个条件中间逗号分隔，输入的条件要保证在javbus有结果返回。
    # 例如：输入'IPZ' 会自动抓取IPZ系列所有磁力（模糊番号抓取耗时较长），建议番号用模糊查询，老师用精准查询，利于分类
    'condition': ['前田かおり'],

    # 抓取优先级
    # ‘清晰度’：自动抓取清晰度高的；
    # ‘字幕’：自动抓取带字幕的，没有字幕抓清晰度高的
    'crawlrule': '清晰度',

    #是否抓取全部磁力
    #'yes': 抓取审核通过的磁力和未经审核的磁力。（只要有磁力就统统抓取！）
    #'no': 只抓取审核通过的磁力
    'crawlall': 'yes'
}

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'JavSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6',
'cache-control': 'max-age=0',
'cookie': '__cfduid=d0df90723d85b000a02f3c71bd4deb1e31571539904; 4fJN_2132_saltkey=hmH09Fbq; 4fJN_2132_lastvisit=1592674908; 4fJN_2132_visitedfid=2D36; PHPSESSID=efnnte1nom2ep9l7c79ec2vom7;',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'JavSpider.middlewares.JavspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'JavSpider.middlewares.RandomUserAgentMiddleware': 400,
   'JavSpider.middlewares.JavspiderDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'JavSpider.pipelines.JavspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
