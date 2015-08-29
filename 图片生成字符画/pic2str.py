from PIL import Image
from scipy import misc
from numpy import *
import numpy as np
name = 'hello.png'
im = Image.open(name)
size = im.size
high = size[1]
width = size[0]

print high,width
new = im.convert('L')
new.save('new%s'%name)
lena = misc.imread('new%s'%name)
for i in range(high):
        for j in range(width):
            if lena[i][j]<128:
                lena[i][j] = 1
            else:
                lena[i][j] = 0
fil = file('code.txt','w+')
x = ndarray.tolist(lena)
for i in range(high):
    for j in range(width):
        if x[i][j] == 0:
            x[i][j] = ' '
        else:
            x[i][j] = '*'
for i in x:
    p = ''.join(i)
    p = '#%s\n'%p
    fil.write(p)
                
fil.close()
            
            
