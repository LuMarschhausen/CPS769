import matplotlib.pyplot as plt

def make_predictions(model, x_input):
    return model.predict(x_input)

def plot_results(data, predictions):
    plt.figure(figsize=(10, 6))
    plt.plot(data[:, 0], data[:, 1], label='Original Path', linestyle='dashed', color='gray')
    plt.plot(predictions[:, 0], predictions[:, 1], label='Predicted Path', color='blue')
    plt.scatter(data[::4, 0], data[::4, 1], color='red')  # Ajustado para plotar pontos únicos
    plt.legend()
    plt.show()
