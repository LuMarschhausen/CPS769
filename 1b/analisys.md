# Análise do Perceptron

## Geração de Dados

Os dados são gerados usando uma distribuição uniforme de pontos em um espaço 2D. Os pontos são classificados em duas classes com base na soma de suas coordenadas.

## Função de Ativação

A função de ativação no perceptron decide se um neurônio deve ser ativado ou não. A função ReLU retorna o valor de entrada diretamente se for positivo; caso contrário, retorna zero. A função Sigmoid, por outro lado, mapeia a entrada para um valor entre 0 e 1.

## Pesos Finais

Após o treinamento, os pesos finais para as funções de ativação ReLU e Sigmoid são:

- ReLU: `{{pesos_relu}}`
- Sigmoid: `{{pesos_sigmoid}}`

## Limites de Decisão

Os limites de decisão para ambas as funções de ativação mostram como o perceptron classifica os pontos no espaço 2D. Diferenças nos limites de decisão são observadas devido às propriedades das funções de ativação.

## Efeito das Funções de Ativação

A função ReLU tende a ser mais eficaz em redes neurais profundas, pois ajuda a mitigar o problema do desvanecimento do gradiente. A função Sigmoid, embora útil em certos contextos, pode saturar e tornar o treinamento mais lento.

## Número de Iterações

O número de iterações afeta o desempenho do perceptron, pois mais iterações geralmente resultam em uma melhor aproximação dos pesos ótimos. No entanto, há um ponto de diminuição dos retornos, onde mais iterações não trazem melhorias significativas.

## Limitações e Melhorias

Um perceptron de camada única tem limitações em tarefas de classificação não linear. Melhorias podem incluir o uso de múltiplas camadas (redes neurais profundas) ou a aplicação de técnicas de regularização para evitar o overfitting.

## Treinamento com Múltiplos Neurônios

Aumentar o número de neurônios em uma camada pode ajudar, mas não resolve totalmente as limitações de um perceptron de camada única para tarefas de classificação complexas. Redes neurais profundas são geralmente mais eficazes para esses problemas.
