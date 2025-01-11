from matplotlib import pyplot as plt
import numpy as np


x=["python","c++","java","javascript"]
y=[85,70,82,84]
z=[20,30,40,50]

width=0.2
p=np.arange(len(x))
p1=[j+width  for j in p]

plt.title("Language")
plt.xlabel("Language")
plt.ylabel("NO")

plt.bar(p,y,width)
plt.bar(p1,z,width)

plt.xticks(p+width/2,x)
plt.legend(["popularity","popularity1"])
plt.show()