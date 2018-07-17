# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)

x = np.arange(20)
y = x**2
plt.figure("Image") # 图像窗口名称
plt.axis('on') # 关掉坐标轴为 off，一般默认是on的
plt.title("Function") # 图像题目
plt.plot(x,y)
plt.show()



print('\n'.join([''.join([('LoveDaLin'[(x-y)%8]
                           if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0
                           else' ')
                          for x in range(-30,30)])
                 for y in range(15,-15,-1)]))