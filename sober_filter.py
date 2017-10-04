
# coding: utf-8

# In[24]:

from PIL import Image
import numpy as np

im = Image.open('./crocodile.jpg')
im = im.convert('RGB')
im = np.array(im)
shape = im.shape

sober_h = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])/8
sober_v = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])/8

hor = np.zeros(shape)
for h in range(shape[0]-3):
    for v in range(shape[1]-3):
        for c in range(shape[2]):
            num = 0
            for hi in range(3):
                for vi in range(3):
                    num += im[h+hi][v+vi][c]*sober_h[hi][vi]
            hor[h+1][v+1][c] = num
            
ver = np.zeros(shape)
for h in range(shape[0]-3):
    for v in range(shape[1]-3):
        for c in range(shape[2]):
            num = 0
            for hi in range(3):
                for vi in range(3):
                    num += im[h+hi][v+vi][c]*sober_v[hi][vi]
            ver[h+1][v+1][c] = num
    
grad = np.zeros(shape)
max_mean = 1
for x in range(shape[0]):
    for y in range(shape[1]):
        hrgb = hor[x,y]
        vrgb = ver[x,y]
        [r,g,b] = np.sqrt(hrgb**2 + vrgb**2)
        mean = np.mean([r,g,b])
        if mean > max_mean:
            max_mean = mean
        grad[x,y] = [mean, mean, mean]
        
grad = np.around(grad*255/max_mean)
#grad = np.ones(shape)*255 - grad

output = Image.fromarray(np.uint8(grad))
output.save('crocodile.bmp')

