#DeZeroのLinearクラスを参考
#とりあえず順伝搬だけできるようにする   
import numpy as np

def linear(x, W, b=None):
    y = np.dot(x, W)
    if b is not None:
        y += b
    return y





