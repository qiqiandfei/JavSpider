# JavSpider
根据老师或车牌去javbus抓取磁力地址的爬虫脚本～

# 配置说明

1、主域名：

设置主域名javbus主站需要fq，没有梯子的请填写放屏蔽地址例如：'https://www.seedmm.cam'

防屏蔽地址不保证永久有效，失效需更换

欧美影片抓取填写地址'https://javbus.one'

默认配置：domain = https://www.javbus.com


2、过滤条件：

过滤条件输入老师姓名，或者番号，支持混合输入，支持模糊输入，多个条件中间逗号分隔，输入的条件要保证在javbus有结果返回。

例如：输入'IPZ' 会自动抓取IPZ系列所有磁力（模糊番号抓取耗时较长），建议番号用模糊查询，老师用精准查询，利于分类

默认配置：condition = 三上悠亜


3、抓取优先级：

‘清晰度’：自动抓取清晰度高的；

‘字幕’：自动抓取带中文字幕的，没有字幕抓清晰度高的

默认配置：crawlrule = 字幕


4、是否抓取全部磁力：

'yes': 抓取审核通过的磁力和未经审核的磁力。（只要有磁力就统统抓取！）

'no': 只抓取审核通过的磁力

默认配置：crawlall = yes


5、骑兵 or 步兵 or 全部 有些女优没有下码影片，请确认后再抓取～ 欧美影片请忽略此设置～

'yes': 只下载骑兵
    
'no': 只下载步兵
    
'all': 全部都要！
    
默认配置：mosaic = all

# 源码运行

运行原生Python需要安装Python3并引入scrapy库及相关依赖；

`pip install -r requirements.txt`

`python crawl.py`

# 二进制运行

**运行之前确保ini配置文件和可执行文件在同一个目录下**

windows: 双击运行javspider_win_amd64.exe

linux: ./javspider_linux_amd64

等待执行结束后，结果文件保存在 CrawlResult文件夹下

# 免责声明
本脚本仅限用于爬虫技术交流，切勿用于非法用途，由于个人行为引发的一切法律后果与本人无关！
