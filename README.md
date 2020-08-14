# JavSpider
根据老师或车牌去javbus抓取磁力地址的爬虫脚本～

# 开发环境
脚本使用Python开发，需要安装Python3并引入scrapy库及相关依赖

引入scrapy库，在命令行下执行：pip install scrapy

# 修改配置
打开脚本目录，进入JavSpider文件夹，找到settings.py。找到‘USER_CONFIG’（17行），按需修改参数。


1、主域名：

设置主域名javbus主站需要fq，没有梯子的请填写放屏蔽地址例如：'https://www.seedmm.cam'

防屏蔽地址不保证永久有效，失效需更换

欧美影片抓取填写地址'https://javbus.one'

默认配置：'domain': ['https://www.javbus.com']


2、过滤条件：

过滤条件输入老师姓名，或者番号，支持混合输入，支持模糊输入，多个条件中间逗号分隔，输入的条件要保证在javbus有结果返回。

例如：输入'IPZ' 会自动抓取IPZ系列所有磁力（模糊番号抓取耗时较长），建议番号用模糊查询，老师用精准查询，利于分类

默认配置：'condition': ['三上悠亜']


3、抓取优先级：

‘清晰度’：自动抓取清晰度高的；

‘字幕’：自动抓取带中文字幕的，没有字幕抓清晰度高的

默认配置：'crawlrule': '字幕'


4、是否抓取全部磁力：

'yes': 抓取审核通过的磁力和未经审核的磁力。（只要有磁力就统统抓取！）

'no': 只抓取审核通过的磁力

默认配置：'crawlall': 'yes'


5、骑兵 or 步兵 or 全部 有些女优没有下码影片，请确认后再抓取～ 欧美影片请忽略此设置～

'yes': 只下载骑兵
    
'no': 只下载步兵
    
'all': 全部都要！
    
默认配置：'mosaic': 'no'


# 运行脚本
1、开始->运行 输入‘cmd’进入命令行

2、cd到项目目录；或者直接在项目目录下‘Shift+鼠标右键’，选择在此处打开命令行或powershell

3、输入命令 scrapy crawl jav  等待程序自动抓取结束(结束标识：INFO: Spider closed (finished))

4、脚本执行结束后，结果目录（CrawlResult）中会生成两个文件 xxx_xxx_info.json和xxx_xxx__magnet.txt；xxx_xxx_info.json保存信息较全，可以作为后续数据处理的数据源；xxx_xxx_magnet.txt为纯磁力，可以直接复制到115离线

# 免责声明
本脚本仅限用于爬虫技术交流，切勿用于非法用途，由于个人行为引发的一切法律后果与本人无关！
