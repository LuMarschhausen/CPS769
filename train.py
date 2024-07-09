def train_model(model, x_train, y_train, epochs=300):
    model.fit(x_train, y_train, epochs=epochs, verbose=0)
