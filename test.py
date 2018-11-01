#!/usr/bin/python
# -*- coding :utf-8 -*-
str="英国之旅三☞康桥流波"
print((str.strip('\n')))
print(str.split('@@'))
print(int(str.split('@@')[4].split('RMB')[0]))
print(str.split('@@')[6])