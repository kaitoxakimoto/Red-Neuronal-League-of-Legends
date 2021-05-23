import numpy as np
import pandas as pd


def load_data_csv(input):
	#Cargar data de csv
	
    x = pd.read_csv(filepath_or_buffer=input, low_memory=False)
    

    return x

def save_data_csv(x_train, x_test, y_train,  y_test):
    np.savetxt('x_train.csv', x_train, delimiter=",", fmt='%s')
    np.savetxt('x_test.csv', x_test, delimiter=",", fmt='%s')
    np.savetxt('y_train.csv', y_train, delimiter=",", fmt='%s')
    np.savetxt('y_test.csv', y_test, delimiter=",", fmt='%s')