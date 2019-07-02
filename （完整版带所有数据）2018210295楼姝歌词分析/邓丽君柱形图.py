# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:36:07 2019

@author: 楼
"""


import pyecharts
from pyecharts import Bar

bar = Bar("邓丽君歌词常用词", "出现次数")
                                #暗色背景色
bar.add("词语",                                        #注解==label
        ["爱","爱人","情","姑娘","夜色","花儿","吹","人生","春风","清平调","西楼","独上","但愿人长久"], #横坐标
        [4, 2, 2, 2, 2, 2,2,2,2,2,2,2,1])                       #纵坐标
bar.render('./denglijunbar.html')                          #文件存储路径（默认保存当前文件路径）