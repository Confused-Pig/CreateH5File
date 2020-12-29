#!/user/bin/python3
# Author:Confused Pig
# -*- coding: utf-8 -*-

# @Time    : 2020/12/28  21:18
# @Author  : Confused Pig
# @Site    : 
# @File    : createH5py.py
# @Software: PyCharm

import os
import numpy as np
import cv2
import h5py

def save_image_to_h5py(path):
    img_list = []
    label_list = []
    dir_counter = 0                  #TwoClass里有两个文件夹，有两类，分别为0,1   dir_counter就为了来方便后面label
                                     #如果你的label不是0,1，是其他或者例如cat，dog类，这里也可以不用它，后面直接用文件名做label
    for child_dir in os.listdir(path):
        child_path = os.path.join(path,child_dir)

        for dir_image in os.listdir(child_path):                        #遍历二级文件每个图片并append信息进数组
            img = cv2.imread(os.path.join(child_path,dir_image))
            img_list.append(img)
            label_list.append(dir_counter)

        dir_counter += 1

    img_np = np.array(img_list)

    label_np = np.array(label_list)
    print('数据集标签顺序：\n',label_np)            #这里我打印了label信息，其对应图片信息，前6张为0，后9张为1
                                                 #所以标签会是[0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 ]

    #'a' ，如果已经有这个名字的h5文件存在将不会打开，目的为了防止误删信息。
    #‘w' ，如果有同名文件也能打开，但会覆盖上次的内容。
    with h5py.File('datasets/cat_or_not.h5','a') as f:
        f.create_dataset('training_cat',data = img_np)              #创建两个数据集，分别为training_cat
        f.create_dataset('training_label',data = label_np)          #和training_label的数组集

        f.close()

#run
save_image_to_h5py('TwoClasses')