
import numpy as np

list=[12,45,67]
list1=[2,3,8]
v1=np.array(list)
v2=np.array(list1)
print("vector1:"+str(v1))
print("vector2:"+str(v2))
n=int(input("input the scalar no:"))
print("scalar produt",n*v1)
print("dot produt of two numberds",np.dot(list,list1))
