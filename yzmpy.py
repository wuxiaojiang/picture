#-*-coding:utf-8-*-
#------------------------------------------------------------------
#程序名：验证码处理
#作 者：biopunk
#日 期：2015/2/28
#------------------------------------------------------------------
from PIL import Image
import pylab as pl
from scipy import misc
from numpy import *
import numpy as np
import urllib
import os
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def l_dir():
    path = os.getcwd()
    d = os.listdir('%s\\train'%path)
    namelist = []
    for i in d:
        namelist.append(i.split('.')[0])
    #timeslist = []
    numlist = []
    for i in namelist:
        numlist.append(int(i.split('_')[0]))
    return numlist,namelist
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def exist(num):
    name = []
    numlist,namelist = l_dir()
    if num in numlist:
        return 1
    else:
        return 0
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def g_tran(num,times):
    numlist,nameslist = l_dir()
    print numlist
    print nameslist
    if exist(num) == 1:
        print u'存在训练文件'
        path = os.getcwd()
        o = open('%s\\train\\%d_%d.txt'%(path,num,times))
        c = o.read()
        arr = arange(96).reshape(12,8)
        for i in range(12):
            for j in range(8):
                arr[i][j] = c[8*i+j]
        return arr
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class yzm():
    def _init_(self):
        pass
    #******************************************************************
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
    #*******************************************************************
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
        list1 = []
        for i in range(5):
            c = arange(96).reshape(12,8)
            for j in range(12):
                for k in range(8):
                    c[j][k] = str(lena[j+5][k+5+9*i])
            list1.append(c)
        return list1
    #********************************************************************
    def tran(self,name,list1):
        im = Image.open(name)
        im.show()
        path = os.getcwd()
        answer = raw_input(u"请输入看见的数字")
        if len(answer) == 5:               
            for i in range(len(answer)):
                o = file('%s\\train\\%s.txt'%(path,answer[i]),'w+')
                #print list1[i]
                for j in range(12):
                    for k in range(8):
                        #print list1[i][j][k]
                        o.write(str(list1[i][j][k]))
                o.close()                        
        else:
            print u'训练失败'
    #**********************************************************************
    def get_tran(self,num,times):
        arr = g_tran(num,times)
        print arr
