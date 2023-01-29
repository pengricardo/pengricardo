#!/usr/bin/env python
# coding: utf-8

# In[14]:


import tkinter
from tkinter import *
import os

# 主要的窗口
root = tkinter.Tk()
root.title('进销存产品管理系统')
root.geometry('400x400')

# 创建框架
frame_list = tkinter.Frame(root)
frame_list.pack()

# 创建列表框
listbox = Listbox(frame_list, width=50, height=15)
listbox.pack()

# 创建按钮
frame_btn = tkinter.Frame(root)
frame_btn.pack(pady=10)

# 查看产品信息按钮
btn_view = tkinter.Button(frame_btn, text='查看产品信息', width=10, command=None)
btn_view.pack(side=LEFT)

# 添加产品信息按钮
btn_add = tkinter.Button(frame_btn, text='添加产品信息', width=10, command=None)
btn_add.pack(side=LEFT)

# 修改产品信息按钮
btn_alter = tkinter.Button(frame_btn, text='修改产品信息', width=10, command=None)
btn_alter.pack(side=LEFT)

# 删除产品信息按钮
btn_delete = tkinter.Button(frame_btn, text='删除产品信息', width=10, command=None)
btn_delete.pack(side=LEFT)

# 运行程序
root.mainloop()

# 定义Product类
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# 定义ProductManager类
class ProductManager:
    def __init__(self):
        self.products = []

# 添加新商品
    def add_product(self, product):
        self.products.append(product)
        print('添加商品 %s 成功' % product.name)

# 删除商品
    def delete_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print('删除商品 %s 成功' % product.name)
                return
        print('没有该商品，无法删除')

# 根据商品名查找商品
    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        print('没有该商品')

# 进货
    def buy_product(self, name, quantity):
        product = self.find_product(name)
        if product is not None:
            product.quantity += quantity
            print('进货 %s 成功' % product.name)

# 出货
    def sell_product(self, name, quantity):
        product = self.find_product(name)
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantit


# In[ ]:




