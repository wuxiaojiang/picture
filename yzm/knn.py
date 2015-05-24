#---------------------------------------------------------
from PIL import Image
import pylab as pl
from scipy import misc
from numpy import *
import numpy as np
import urllib
import os
import re
import operator
#---------------------------------------------------------
def get():
    url = 'http://211.70.49.127/CheckCode.aspx'
    web = urllib.urlopen(url)
    pic = web.read()
    name = 'checkcode.png'
    fil = file(name,'wb')
    fil.write(pic)
    fil.flush()
    fil.close
    url = web.geturl()
    p_url = re.findall(r'http://211.70.49.127/(.*?)/CheckCode.aspx',url)
    part_url = p_url[0]
    return name,part_url
#------------------------------------------------------------------------------
def p2m(name):
    im = Image.open(name)
    new = im.convert('L')
    new.save('new%s'%name)
    lena = misc.imread('new%s'%name)
    for i in range(22):
        for j in range(60):
            if lena[i][j]<128:
                lena[i][j] = 1
            else:
                lena[i][j] = 0
    list1=[]
    for i in range(5):
        c = arange(96).reshape(96)
        p = 0
        for j in range(12):
            for k in range(8):
                c[p] = int(lena[j+5][k+5+9*i])
                p+=1
        list1.append(c)
    return list1
#---------------------------------------------------------------------------------
def file_open():
    path = os.getcwd()
    list2=[]
    for i in range(10):
        txt = open('%s/train/%s.txt'%(path,i))
        text = txt.read()
        c = arange(96).reshape(96)
        for j in range(96):
            c[j] = text[j]
        list2.append(c)
        txt.close
    test_array = array([list2[0],
                        list2[1],
                        list2[2],
                        list2[3],
                        list2[4],
                        list2[5],
                        list2[6],
                        list2[7],
                        list2[8],
                        list2[9]])
    return test_array
#-----------------------------------------------------------------------------------
def classify(inx,dataset,labels,k):
    dataset_size = dataset.shape[0]
    diff_mat = tile(inx,(dataset_size,1))-dataset
    #print diff_mat
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5
    sort_distances = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sort_distances[i]]
        class_count[vote_label] = class_count.get(vote_label,0)+1
    sorted_class_count = sorted(class_count.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sorted_class_count[0][0]

#--------------------------------------------------------------------------
if __name__ == '__main__':
    name,part_url = get()
    name = 'checkcode.png'
    list1 = p2m(name)
    list2 = file_open()
    #print list2
    cheak_code = []
    for j in range(5):
        labels =[i for i in range(10)]
        c =  classify(list1[j],list2,labels,1)
        cheak_code.append(str(c))
        check = ''.join(cheak_code)
    print check
