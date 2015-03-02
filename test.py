import yzmpy
y = yzmpy.yzm()
name = y.get()
list1 = y.p_to_a(name)

#for i in list1:
#    print i
y.tran(name,list1)
#y.get_tran(0,1)

