# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:59:41 2019

@author: 楼
"""


import pyecharts
from pyecharts import Bar

bar = Bar("beyond歌词常用词", "出现次数")
                                #暗色背景色
bar.add("词语",                                        #注解==label
        ["心","一生","理想","拥有","爱","节奏","唏嘘","自由","天空","创伤","风雨","世间","挣扎"], #横坐标
        [12,12, 9, 8,8, 7,7,6,5,5,5,5,5])                       #纵坐标
bar.render('./beyondbar.html')                          #文件存储路径（默认保存当前文件路径）