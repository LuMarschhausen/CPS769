from tensorflow.keras import layers, models

def create_model(input_shape):
    model = models.Sequential([
        layers.LSTM(50, activation='relu', input_shape=input_shape),
        layers.Dense(2)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model
