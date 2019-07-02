# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:05:28 2019

@author: 楼
"""

from pyecharts import Pie

attr = ["心","一生","理想","拥有","爱","节奏","唏嘘","自由","天空","创伤","风雨","世间","挣扎"]
v1 = [12,12, 9, 8,8, 7,7,6,5,5,5,5,5]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render('./beyondpie.html')