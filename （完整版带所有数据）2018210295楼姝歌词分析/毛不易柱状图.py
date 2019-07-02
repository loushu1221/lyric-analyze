# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:05:05 2019

@author: 楼
"""

import pyecharts
from pyecharts import Bar

bar = Bar("毛不易歌词常用词", "出现次数")
                                #暗色背景色
bar.add("词语",                                        #注解==label
        ["智慧","大狗","唧唧","想","走","时光","明天","爱","忘","岁月","生活","哭","远方"], #横坐标
        [17, 16, 15, 13, 11, 11,9,9,9,9,8,8,8])                       #纵坐标
bar.render('./maobuyibar.html')                          #文件存储路径（默认保存当前文件路径）
