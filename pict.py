from scipy import misc
import pylab as pl
lena = misc.imread('new.png')
print type(lena)
for i in range(22):
    print lena[i]
    for j in range(60):
        if lena[i][j]<123:
            lena[i][j]=1
        else:
            lena[i][j]=0
text = file('bat.txt','w+')
for i in range(22):
    text.write('\n')
    for j in range(60):
        text.write(str(lena[i][j]))
text.close
