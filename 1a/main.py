import os
from data import prepare_data
from model import create_model
from train import train_model
from predict import make_predictions, plot_results

# Desabilitar GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Preparar os dados
x_train, y_train, data = prepare_data()

# Criar o modelo
model = create_model(input_shape=(x_train.shape[1], x_train.shape[2]))

# Treinar o modelo
train_model(model, x_train, y_train)

# Fazer previsões
predictions = make_predictions(model, x_train[:5])

# Plotar os resultados
plot_results(data, predictions)
