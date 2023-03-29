import numpy as np
import matplotlib.pylab as plt
import pandas as pd

def data():
    x = np.random.rand(100, 1)

        # ww          ww           ww
        #   ww       ww ww       ww
        #     ww    ww   ww    ww
        #       wwww       wwww
        #       wwww       wwww
        
    y = np.cos(x*4*np.pi ) + np.random.rand(100, 1)
    True_label = np.cos(x*4*np.pi)
    
    plt.scatter(x, y)
    plt.show()

    df = pd.DataFrame(np.hstack((x,y,True_label)), columns=['x', 'y','True_label'])
    df.to_csv('data.csv', index=False)

    return x, y

if __name__ == '__main__':
    data()
