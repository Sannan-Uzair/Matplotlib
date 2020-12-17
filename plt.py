import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,5,10)
y = x**2
plt.plot(x,y)
plt.title("Days Squared Chart")
plt.xlabel("Days")
plt.ylabel("Days Squared")

plt.subplot(1,2,1) # 1 Row 2 Column and 1 plot
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(x,y,'b')
# plt.show()

fig1 = plt.figure(figsize=(5,4),dpi=100) # 5 width, 4 heihgt( we can say 5 by 4)
axis = fig1.add_axes([0.1, 0.1, 0.9, 0.9]) #0.1 left, 0.1 bottom, 0.9 width, 0.9 height
axis.set_xlabel('Days')
axis.set_ylabel('Days Squared')
axis.set_title("Days Squared Chart")
axis.plot(x,y,label='x/x**2')
axis.plot(y,x,label='x**2/x')
axis.legend(loc=0)
# plt.show()

fig1 = plt.figure(figsize=(5,4),dpi=100) # 5 width, 4 heihgt( we can say 5 by 4)
axis = fig1.add_axes([0.1, 0.1, 0.9, 0.9]) #0.1 left, 0.1 bottom, 0.9 width, 0.9 height
axis.set_xlabel('Days')
axis.set_ylabel('Days Squared')
axis.set_title("Days Squared Chart")
axis.plot(x,y,label='x/x**2')
axis.plot(y,x,label='x**2/x')
axis.legend(loc=0)

axis2 = fig1.add_axes([0.45, 0.45, 0.4, 0.3])
axis2.set_xlabel('Days')
axis2.set_ylabel('Days Squared')
axis2.set_title('Days Squared Chart')
axis2.plot(x,y,'r')
axis2.text(0,40,'Message')
plt.show()