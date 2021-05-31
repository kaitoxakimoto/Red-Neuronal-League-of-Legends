from random import seed
from random import random

import utility as ut
from sklearn.model_selection import train_test_split ##solo usamos sklearn para repartir los datos
from nerualNetwork import *
import numpy as np
import time






xe = ut.load_data_csv("games.csv")


x = xe.drop(['gameId','winner', 'seasonId'], axis=1)
y = xe.winner
y = y.replace(1,0)
y = y.replace(2,1)


x = (x - np.min(x)) / (np.max(x) - np.min(x))

x_train, x_test, y_train,  y_test = train_test_split(x,y, train_size=0.7, test_size=0.3, random_state=4) #ramdon state es para que no sea random la repartición realmente
ut.save_data_csv(x_train, x_test, y_train,  y_test)



print(x_train.shape[1])

nn = NeuralNetwork([x_train.shape[1],x_train.shape[1]*2 + 1, int(x_train.shape[1]/2) + 1, x_train.shape[1]+1,1])

iteraciones = 10000000

start_time = time.time()
nn.train(np.array(x_train), np.array(y_train), learning_rate=0.03,epochs=iteraciones)
 

print("Tiempo training: %s segundos ---" % (time.time() - start_time))

index=0




#nn.print_weights()#
index=0

start_time = time.time()

predicciones = nn.predict(np.array(x_test))

# for e in np.array(x_test):
    
#     #print("\nPartida: ", index+1, "\nGanador: Equipo ", 1+int(np.round(nn.predict(e))))
# # # # #     # print(e)
#     #print(nn.predict(e))
#     predicciones.append(nn.predict(e))

#     index=index+1
# # # #     index=index+1

# print(predicciones)

# from sklearn.metrics import precision_recall_fscore_support as score



# precision, recall, fscore, support = score(np.array(y_test), predicciones)

# print('precision: {}',precision)
# print('recall: {}'.format(recall))
# print('fscore: {}'.format(fscore))
# print('support: {}'.format(support))

predictCount=0

for i in range(len(predicciones)):
    if predicciones[i]==np.array(y_test)[i]:
        predictCount=predictCount+1


print("Tiempo testing: %s segundos ---" % (time.time() - start_time))  
print("Con un total de ", iteraciones," iteraciones, la precisión total es: ", predictCount/len(predicciones) * 100, "%" )