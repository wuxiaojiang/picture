from PIL import Image
import pylab as pl
from scipy import misc
from numpy import *
import numpy as np
im = Image.open('1.png')
new = im.convert('L')
new.save('new.png')

c0 = arange(96).reshape(12,8)
c1 = arange(96).reshape(12,8)
c2 = arange(96).reshape(12,8)
c3 = arange(96).reshape(12,8)
c4 = arange(96).reshape(12,8)

lena = misc.imread('new.png')
for i in range(22):
    for j in range(60):
        if lena[i][j] < 128:
            lena[i][j]=1
        else:
            lena[i][j]=0

for i in range(12):
    for j in range(8):
        c0[i][j] = str(lena[i+5][j+5])
for i in range(12):
    for j in range(8):
        c1[i][j] = str(lena[i+5][j+14])
for i in range(12):
    for j in range(8):
        c2[i][j] = str(lena[i+5][j+23])
for i in range(12):
    for j in range(8):
        c3[i][j] = str(lena[i+5][j+32])
for i in range(12):
    for j in range(8):
        c4[i][j] = str(lena[i+5][j+41])
print c0
print c1
print c2
print c3
print c4


text = file('7.txt','w+')
for i in range(12):
    if i >0:
        text.write('\n')
    for j in range(8):
        text.write(str(c0[i][j]))
text.close
