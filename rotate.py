# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 00:03:53 2017 by Shion Honda
"""

from PIL import Image
import numpy as np

im = Image.open('./profile.bmp')
im = np.array(im)
shape = im.shape

# 回転行列
theta = np.pi
rot = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# 回転変換
rotated = np.zeros(shape)
for x in range(shape[0]):
    for y in range(shape[1]):
        [r, g, b] = im[x,y]
        # 画像の中心を基準とする
        position = np.matrix([[x - shape[0]/2],[y - shape[1]/2]])
        position2 = rot * position
        x2 = int(position2[0,0])
        y2 = int(position2[1,0])
        # 範囲内なら代入
        if -shape[0]/2 < x2 and x2 < shape[0]/2 and -shape[1]/2 < y2 and y2 < shape[1]:
            rotated[x2-int(shape[0]/2),y2-int(shape[1]/2)] = [r,g,b]

output = Image.fromarray(np.uint8(rotated))
output.save("profile_sober.bmp")