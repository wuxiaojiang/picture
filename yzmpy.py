#-*-coding:utf-8-*-
#------------------------------------------
#程序名：验证码处理
#作 者：biopunk
#日 期：2015/2/28
#------------------------------------------
from PIL import Image
import pylab as pl
from scipy import misc
from numpy import *
import numpy as np
import urllib
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class yzm():
    def _init_(self):
        pass
    def get(self):
        web = urllib.urlopen('http://211.70.49.127/CheckCode.aspx')
        pic = web.read()
        name = 'checkcode.png'
        fil = file(name,'wb')
        fil.write(pic)
        fil.flush()
        fil.close
        print '验证码获取成功'
        return name
    def p_to_a(self,name):
        im = Image.open(name)
        new = im.convert('L')
        new.save('new%s'%name)
        lena = misc.imread('new%s'%name)
        for i in range(22):
            for j in range(60):
                if lena[i][j]<128:
                    lena[i][j] = 1
                else:
                    lena[i][j]=0
        c = arange(96).reshape(12,8)
        list1 = []
        for i in range(5):
            for j in range(12):
                for k in range(8):
                    c[j][k] = str(lena[j+5][k+5+9*i])
            list1.append(c)
        return list1
                    
            
        
