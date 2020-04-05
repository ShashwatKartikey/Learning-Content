import numpy as np
from  matplotlib import pyplot as plt
l,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10 = np.loadtxt('data.txt',
                 unpack=True,
                 delimiter = '	',skiprows=1)

for i in range (999):
	for j in range(1,10):
		for k in range (j+1,10):
			if (l[i]==1):
				choice='ro'
			else: 
				choice='bo'
			a='f'+str(j)
			b='f'+str(k)
			x=a[i]
			y=b[i]
			plt.plot(x,y,choice)
			c='feature'+str(j)
			d='feature'+str(k)
			plt.ylabel(d)
			plt.xlabel(c)
			plt.title(c+' vs '+d)
			plt.show()

