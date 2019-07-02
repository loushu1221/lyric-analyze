# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:15:33 2019

@author: 楼
"""

from pyecharts import Pie

attr = ["智慧","大狗","唧唧","想","走","时光","明天","爱","忘","岁月","生活","哭","远方"]
v1 = [17, 16, 15, 13, 11, 11,9,9,9,9,8,8,8]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render('./maobuyipie.html')