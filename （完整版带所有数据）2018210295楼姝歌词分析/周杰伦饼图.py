# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:43:58 2019

@author: 楼
"""

from pyecharts import Pie

attr = ["爱","希望","浪漫","故事","泪","微笑","公主","温暖","美丽","梦境","魔术","骑士","兰亭序"]
v1 = [7,4,3,3,3,2,2,2,2,2,2,2,1]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render('./zhoujielunpie.html')