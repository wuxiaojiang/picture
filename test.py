import yzmpy
y = yzmpy.yzm()
name = y.get()
list1 = y.p_to_a(name)
for i in list1:
    print i
