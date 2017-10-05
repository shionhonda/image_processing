# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 23:59:04 2017 by Shion Honda
"""

from PIL import Image
import numpy as np

nm = 'i'

im = Image.open('pics/' + nm + '_bi.bmp')
im = np.array(im)

def diliate(x,y):
    if im[x,y][0] == 255:
        im[x,y] = [0,0,0]
        flags[x,y] = 0
        
def whole_diliate(im, flags):
    for x in range(1,shape[0]-1):
        for y in range(1,shape[0]-1):
            if im[x,y][0]==0 and flags[x,y]==1:
                diliate(x-1,y-1)
                diliate(x,y-1)
                diliate(x+1,y-1)
                diliate(x-1,y)
                diliate(x+1,y)
                diliate(x-1,y+1)
                diliate(x,y+1)
                diliate(x+1,y+1)

def erode(x,y):
    if im[x,y][0] == 0:
        im[x,y] = [255,255,255]
        flags[x,y] = 0
        
def whole_erode(im, flags):
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
            if im[x,y][0]==255 and flags[x,y]==1:
                erode(x-1,y-1)
                erode(x,y-1)
                erode(x+1,y-1)
                erode(x-1,y)
                erode(x+1,y)
                erode(x-1,y+1)
                erode(x,y+1)
                erode(x+1,y+1)

shape = im.shape
# 膨張
flags = np.ones([shape[0],shape[1]])
whole_diliate(im, flags)
# 縮小
flags = np.ones([shape[0],shape[1]])
whole_erode(im, flags)

output = Image.fromarray(np.uint8(im))
output.save("pics/" + nm + "_close.bmp")