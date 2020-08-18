# -*- coding: utf-8 -*-
"""
 * Create by: yufei
 * Date: 2020/8/18
 * Time: 18:04
 * Name: 
 * Porpuse: 
 * Copyright © 2020年 Fei. All rights reserved.
"""
import configparser
import os

'''
读取配置文件
'''
class ReadConfig:
    def __init__(self):
        curpath = os.getcwd()
        configpath = os.path.join(curpath, 'config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath, encoding='utf-8')

    def get_markconfig(self, param):
        value = self.cf.get("javconfig", param)
        return value