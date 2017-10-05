# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:01:22 2017 by Shion Honda
"""

from PIL import Image
import numpy as np

nm = 'crocodile'

im = Image.open(nm + '.bmp')
im = np.array(im)
shape = im.shape
#th3 = 191
th = 50
for x in range(shape[0]):
    for y in range(shape[1]):
        if im[x,y][0] <= th:
            im[x,y] = np.zeros(3)
        else:
            im[x,y] = 255*np.ones(3)

output = Image.fromarray(np.uint8(im))
output.save(nm + "_bi.bmp")
