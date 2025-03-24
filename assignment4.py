tup = ('lahore', 'karachi')
ls = list (tup)
print ("ls")



tup1 = ("faisalabad","jaranwala" , "lahore")
tup2 = ( 1,2,3,4,5,6 )
tup3 = tup2 + tup1
print(tup3[6:] + tup3[:6])
ls = list(tup3)
ls2 =[]

for i in ls:
    ls2.insert(0, i)
print(ls2)
tup4 = tuple(ls2)
print(tup4)

