import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.random.rand(100, 1)

    # ww          ww           ww
    #   ww       ww ww       ww
    #     ww    ww   ww    ww
    #       wwww       wwww
    #       wwww       wwww
    
y = np.cos(4 * np.pi * x) + np.random.rand(100, 1)
#y =np.cos(x)+np.random.rand(100,1)
#y = np.sin(x)+np.random.rand(100,1)




plt.figure(figsize=(10, 7.5))
plt.scatter(x, y) # 散布図
plt.xlabel('x') # x軸ラベル
plt.ylabel('y') # y軸ラベル
plt.suptitle('dataset', fontsize=20) # 図全体のタイトル
plt.title('N=' + str(len(x)), loc='left') # タイトル
plt.grid() # グリッド線
plt.show()
