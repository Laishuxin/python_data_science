# 导入3d模块
# 导入子模块后，想要在普通坐标轴加入projection='3d'就可以创建3维坐标轴
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 200

fig = plt.figure()
ax = plt.axes(projection='3d')
plt.show()