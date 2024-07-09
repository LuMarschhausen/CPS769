import numpy as np

def prepare_data():
    square_path = np.array([
        [0.25, 0.25],
        [0.75, 0.25],
        [0.75, 0.75],
        [0.25, 0.75],
        [0.25, 0.25]
    ])

    num_repeats = 4
    data = np.tile(square_path, (num_repeats, 1))

    x_train = data[:-1].reshape(-1, 1, 2)
    y_train = data[1:].reshape(-1, 2)

    return x_train, y_train, data
