#!/usr/bin/python
# -*- coding :utf-8 -*-
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np
from PIL import Image
import time
def pictureshow(path):
	print(path,type(path))
	picture=Image.open('F:\研一上\云计算\第一次实践作业\wordcloud\\'+path+'.png')
	picture.show()
	time.sleep(5)
	picture.close()
# 	lena=mpimg.imread('F:\研一上\云计算\第一次实践作业\wordcloud\\'+path+'.png')
#  # 读取和代码处于同一目录下的 lena.png
# # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
# # 	plt.rcParams['font.sans-serif'] = ['SimHei']
# # 	plt.rcParams['axes.unicode_minus'] = False
# # 	path=plt.title(path)
# # 	print(type(path))
# 	plt.title(path)
# 	lena.shape  # (512, 512, 3)
# 	path.imshow(lena)  # 显示图片
# 	path.axis('off')  # 不显示坐标轴
# 	path.show()
# 	path.close()

	# time.sleep(5)

pictureshow('Japan')
pictureshow('Qinghai')
pictureshow('Swiss')
pictureshow('Thailand')
pictureshow('UK')

