# -*- coding: utf-8 -*-
"""
 * Create by: yufei
 * Date: 2020/8/19
 * Time: 7:28
 * Name: 
 * Porpuse: 
 * Copyright © 2020年 Fei. All rights reserved.
"""
data = '''
[settings]
default = JavSpider.settings
[deploy]
# url = http://localhost:6800/
project = JavSpider
'''

with open('scrapy.cfg', 'w') as f:
    f.write(data)