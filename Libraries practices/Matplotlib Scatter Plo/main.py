from matplotlib import pyplot as plt
# import numpy as np
# import random
x=[10,20,5,3,7,20,5,15,7,8]
y=["denmark","brazil","Australia","england","southafrica","pakistan","india","china","japan","korea"]
ex=[0.0,0.1,0.0,0.0,0.0,0.1,0.0,0.0,0.0,0.0]
plt.pie(x,labels=y,explode=ex,autopct="%0.1f%%",shadow=True,radius=1,labeldistance=0.9)
plt.title("All countries")
plt.legend(loc=1)
plt.show()