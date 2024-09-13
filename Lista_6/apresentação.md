
Desenvolvi uma aplicação como parte da Lista de Exercícios 6, cujo objetivo principal era criar um sistema capaz de responder perguntas sobre a Qualidade de Experiência (QoE) 
na transmissão de vídeo, utilizando APIs de linguagem natural da OpenAI. A ideia central foi criar uma interface que permitisse aos usuários fazer perguntas sobre o desempenho 
do sistema de streaming, com base nos dados fornecidos de bitrate e latência. Organizei o projeto na pasta "Lista_6" com uma estrutura que segrega o código em módulos bem definidos, 
facilitando a manutenção e a expansão da aplicação. Dentro da pasta "src", criei diferentes arquivos Python para cada responsabilidade do projeto. No arquivo data_processing.py, 
implementei funções específicas para carregar e processar os dados de bitrate e latência fornecidos em formato Excel. Separei essas funções para manter o código organizado e garantir 
que o tratamento de dados fosse feito de forma eficiente. Realizei o merge dos datasets com base nos pares client-server-timestamp, além de converter a coluna de latência (RTT) para 
um formato numérico, prevenindo erros nos cálculos subsequentes. O cálculo da Qualidade de Experiência foi implementado no arquivo qoe_calculation.py. Nesse módulo, criei uma função que 
calcula a QoE dividindo o bitrate pela latência, aplicando esse cálculo a cada entrada do conjunto de dados. A escolha por manter o cálculo em um arquivo separado permite que futuras alterações 
ou melhorias na fórmula de cálculo sejam feitas sem complicar outras partes do código, mantendo a modularidade e a clareza da aplicação. O arquivo function_calling.py é o núcleo da aplicação, 
responsável por interpretar as perguntas dos usuários e fornecer respostas baseadas na análise dos dados. Para isso, implementei diversas lógicas para responder perguntas como: 
"Qual cliente tem a pior QoE?", "Qual é o servidor com a QoE mais consistente?", e "Como a mudança de latência afeta a QoE?". Para cada tipo de pergunta, desenvolvi uma lógica específica, 
utilizando cálculos de média, variância, e simulações para avaliar o impacto de mudanças nos parâmetros, como o aumento de latência.
Por fim, o arquivo main.py coordena a execução de todos os módulos, chamando as funções de carregamento e processamento de dados, cálculo de QoE, e interpretação das perguntas dos usuários. 
Esse arquivo foi mantido como ponto central de execução, fazendo as chamadas das funções e permitindo que o sistema interaja com o usuário de forma clara e direta. A divisão do código em módulos 
distintos, com responsabilidades bem definidas, garante que a aplicação seja organizada, escalável e de fácil manutenção, atendendo aos requisitos da Lista de Exercícios 6 de maneira eficiente e 
estruturada.