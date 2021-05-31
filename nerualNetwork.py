import numpy as np
np.warnings.filterwarnings('ignore', 'overflow')

def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))     # Define sigmoid function
    sig = np.minimum(sig, 0.9999)  # Set upper bound
    sig = np.maximum(sig, 0.0001)  # Set lower bound
    return sig

def sigmoid_derivada(x):
    return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_derivada(x):
    return 1.0 - x**2


class NeuralNetwork:

    def __init__(self, layers):
        
        # Se iniciando las variables de peso
        self.weights = []
        self.deltas = []
        
        # función random para asignar valores entre -1 y 1
        for i in range(1, len(layers) - 1):
            r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
            self.weights.append(r)
        # valores aleatorios a la salida
        r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
        
        self.weights.append(r)

    def train(self, X, y, learning_rate=0.2, epochs=100000):
        
        # Se le agrega el bias a la capa de entrada
        
        ones = np.atleast_2d(np.ones(X.shape[0]))
        #print(ones)
        X = np.concatenate((ones.T, X), axis=1)
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]

            for l in range(len(self.weights)):
                    dot_value = np.dot(a[l], self.weights[l])
                    activation = sigmoid(dot_value)
                    a.append(activation)
           
            #se calcula la diferencia entre el error de la ultima predicción realizada y el valor esperado
            error = y[i] - a[-1]
            # print("error: ", error)
            deltas = [error * sigmoid_derivada(a[-1])]
            
            # Se empieza el calculo de las deltas desde el segundo hasta el ultimo
            # (Una capa anterior a la de salida)
            for l in range(len(a) - 2, 0, -1): 
                deltas.append(deltas[-1].dot(self.weights[l].T)*sigmoid_derivada(a[l]))
            self.deltas.append(deltas)

            # Se invierten los deltas
            deltas.reverse()

            # backpropagation
            # Se multiplican los deltas ded salicas con la transpuesta de las actividades de entrada
            #    
            # Se actualiza  el peso sumandole  el gradiente por la tasa de aprendizaje
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

            if k % 10000 == 0: print('Iteración: ', k)

    def predict(self, x): 
        
        
        ones = np.atleast_2d(np.ones(x.shape[0]))
        a = np.concatenate((ones.T, x), axis=1)
        #print(len(self.weights))
        for l in range(0, len(self.weights)):
            # print(self.weights[l])
            #print("AAAA: ", sigmoid(np.dot(a, self.weights[l])))
            a = sigmoid(np.dot(a, self.weights[l]))
        return np.rint(a)

    def print_weights(self):
        print("LISTADO PESOS DE CONEXIONES")
        print((len(self.weights)))
        for i in range(len(self.weights)):
            
            print(self.weights[i])

    def get_deltas(self):
        return self.deltas