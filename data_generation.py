import numpy as np
import matplotlib.pyplot as plt

def generate_data(num_points=100):
    X = np.random.rand(num_points, 2)
    y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Classificação baseada na soma das coordenadas
    return X, y

def plot_data(X, y):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Data Distribution')
    plt.show()

if __name__ == "__main__":
    X, y = generate_data()
    plot_data(X, y)
