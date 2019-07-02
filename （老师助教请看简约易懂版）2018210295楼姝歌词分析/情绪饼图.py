# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:08:43 2019

@author: 楼
"""

from pyecharts import Pie

attr = ["正面","负面"]
v1 = [0.974436342974455, 0.02556365702554497]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render('./maobuyiqingxubingtu.html')