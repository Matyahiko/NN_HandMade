import numpy as np
import matplotlib.pylab as plt
import linear
import sigmoid
import pandas as pd

def main():

    df = pd.read_csv('data.csv')
    x = df['x'].values
    y = df['y'].values

    x_len = len(x)

    hidden1_node = 50
    hidden2_node = 25

    #重み
    #100*50
    W1 = np.zeros(x_len,hidden1_node)
    #50*25
    W2 = np.zeros(hidden1_node,hidden2_node)
    
    #バイアスの初期化
    b1 = np.zeros(hidden1_node)
    b2 = np.zeros(hidden2_node)
    epoc = 100

    for i in epoc:
        #順伝搬
        #100*50
        a1 = linear.linear(x,W1,b1)
        #100*50
        z1 = sigmoid.sigmoid(a1)
        #100*25
        a2 = linear.linear(z1,W2,b2)
        #100*25
        z2 = sigmoid.sigmoid(a2)

        #逆伝搬




if __name__ == '__main__':
    main()
