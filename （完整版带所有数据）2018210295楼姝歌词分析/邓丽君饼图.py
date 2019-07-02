# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:40:03 2019

@author: 楼
"""

from pyecharts import Pie

attr = ["爱","爱人","情","姑娘","夜色","花儿","吹","人生","春风","清平调","西楼","独上","但愿人长久"]
v1 = [4, 2, 2, 2, 2, 2,2,2,2,2,2,2,1]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render('./denglijunpie.html')