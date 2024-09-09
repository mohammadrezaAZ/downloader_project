import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,10,30])
y = np.array([1,10,30])
#plt.plot(x,y,'*')
#plt.plot(y,marker='o')
# plt.plot(y, 'o--b', ms = 20, mec = 'r',mfc = 'g')
# plt.plot(y, linestyle = 'dotted', color= 'red')
# plt.plot(y, linewidth = 30)
plt.plot(x,y,'o:r')
font1 = {'family':'serif','color':'blue','size':20}
plt.title('Salary Prediction',fontdict=font1, loc = 'left')
plt.xlabel('Salary')
plt.ylabel('Experience Year')


plt.show()