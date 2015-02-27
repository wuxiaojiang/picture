from PIL import Image
import pylab as pl
from scipy import misc
from numpy import *
im = Image.open('1.png')
new = im.convert('L')
new.save('new.png')
c = random.rand(12,8)
lena = misc.imread('new.png')
for i in range(22):
    for j in range(60):
        if lena[i][j] < 128:
            lena[i][j]=1
        else:
            lena[i][j]=0
for i in range(12):
    for j in range(8):
        c[i][j] = lena[i+5][j+14]
text = file('3.txt','w+')
for i in range(12):
    if i >0:
        text.write('\n')
    for j in range(8):
        text.write(str(int(c[i][j])))
text.close
