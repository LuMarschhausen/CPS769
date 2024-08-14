import numpy as np
import matplotlib.pyplot as plt
from perceptron import Perceptron
from data_generation import generate_data

def plot_decision_boundary(perceptron, X, y, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = np.array([perceptron.predict(np.array([x, y])) for x, y in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    X, y = generate_data()
    
    # Perceptron com ReLU
    perceptron_relu = Perceptron(input_size=2, activation_function='relu')
    perceptron_relu.train(X, y, epochs=1000, lr=0.01)
    plot_decision_boundary(perceptron_relu, X, y, "Limite de Decisão com ReLU")
    
    # Perceptron com Sigmoid
    perceptron_sigmoid = Perceptron(input_size=2, activation_function='sigmoid')
    perceptron_sigmoid.train(X, y, epochs=1000, lr=0.01)
    plot_decision_boundary(perceptron_sigmoid, X, y, "Limite de Decisão com Sigmoid")
