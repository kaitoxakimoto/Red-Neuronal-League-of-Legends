from random import seed
from random import random

import utility as ut
from sklearn.model_selection import train_test_split ##solo usamos sklearn para repartir los datos
from nerualNetwork import *
import numpy as np
import pandas as pd

def main():
    par_sae, par_sft = ut.load_config()
    xe = ut.load_data_csv("games.csv")
    W, Xr = train(xe, par_sae)
    #Ws, cost = train_softmax(Xr, ye, par_sft)
    ut.save_w_dl(W, "w_dl.npz", "cost_sofmax.csv")




xe = ut.load_data_csv("games.csv")


x = xe.drop(['gameId','winner', 'seasonId'], axis=1)
y = xe.winner

x = (x - np.min(x)) / (np.max(x) - np.min(x))

x_train, x_test, y_train,  y_test = train_test_split(x,y, train_size=0.7, test_size=0.3, random_state=4) #ramdon state es para que no sea random la repartición realmente
ut.save_data_csv(x_train, x_test, y_train,  y_test)



print(x_train.shape[1])

nn = NeuralNetwork([x_train.shape[1],x_train.shape[1]*2 + 1,1])




nn.fit(np.array(x_train), np.array(y_train), learning_rate=0.003,epochs=20001)
 
index=0




nn.print_weights()
for e in np.array(x_test):
# # # #     # print(e)
    nn.predict(e)
# # # #     index=index+1

