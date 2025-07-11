
l1=[2,4,5,8,9]
l2=[1,2,3,6,7,8]
print("list 1=",l1)
print("list 2=",l2)
un=set(l1)|set(l2)
print("union",list(un))
intr=set(l1)&set(l2)
print("intersection",list(intr))


