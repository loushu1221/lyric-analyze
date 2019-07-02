# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:43:28 2019

@author: 楼
"""

attr = ["正面","负面"]
v1 = [0.9247468349346561,0.07525316506534384]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render('.denglijunqingxubingtu.html')