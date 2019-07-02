# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:43:56 2019

@author: 楼
"""



import pyecharts
from pyecharts import Bar

bar = Bar("周杰伦歌词常用词", "出现次数")
                                #暗色背景色
bar.add("词语",                                        #注解==label
        ["爱","希望","浪漫","故事","泪","微笑","公主","温暖","美丽","梦境","魔术","骑士","兰亭序"], #横坐标
        [7,4,3,3,3,2,2,2,2,2,2,2,1])                       #纵坐标
bar.render('./zhoujielunbar.html')                          #文件存储路径（默认保存当前文件路径）