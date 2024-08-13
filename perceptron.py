import numpy as np

class Perceptron:
    def __init__(self, input_size, activation_function='relu'):
        self.weights = np.random.rand(input_size + 1)  # Inclui o peso do bias
        self.activation_function = activation_function

    def activation(self, x):
        if self.activation_function == 'relu':
            return np.maximum(0, x)
        elif self.activation_function == 'sigmoid':
            return 1 / (1 + np.exp(-x))
        else:
            raise ValueError("Função de ativação desconhecida")

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return self.activation(summation)

    def train(self, training_inputs, labels, epochs=100, lr=0.01):
        for _ in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights[1:] += lr * error * inputs
                self.weights[0] += lr * error
