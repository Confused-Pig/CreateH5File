#!/user/bin/python3
# Author:Confused Pig
# -*- coding: utf-8 -*-

# @Time    : 2020/12/28  22:54
# @Author  : Confused Pig
# @Site    : 
# @File    : readH5py.py
# @Software: PyCharm


import numpy as np
import matplotlib.pyplot as plt
import h5py


with h5py.File('datasets/cat_or_not.h5',"r") as f:
    for key in f.keys():
        print(f[key],key,f[key].name)
    f.close()


#load h5py datas
train_datas = h5py.File('datasets/cat_or_not.h5','r')
training_cat = np.array(train_datas['training_cat'][:])
plt.imshow(training_cat[3])
plt.show()
train_datas.close()
