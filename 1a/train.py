import numpy as np
from perceptron import Perceptron
from data_generation import generate_data, plot_data

# Gerar dados
X, y = generate_data()

# Treinar perceptron com ReLU
perceptron_relu = Perceptron(input_size=2, activation_function='relu')
perceptron_relu.train(X, y, epochs=1000, lr=0.01)

# Treinar perceptron com Sigmoid
perceptron_sigmoid = Perceptron(input_size=2, activation_function='sigmoid')
perceptron_sigmoid.train(X, y, epochs=1000, lr=0.01)

# Mostrar pesos finais
print("Pesos finais com ReLU:", perceptron_relu.weights)
print("Pesos finais com Sigmoid:", perceptron_sigmoid.weights)

# Plotar dados
plot_data(X, y)
