import pandas as pd
from pandasql import sqldf

# Carregar o CSV em um DataFrame
colunas = ['DATA (YYYY-MM-DD)', 'Hora UTC', 'TEMPERATURA DO PONTO DE ORVALHO (°C)']
df = pd.read_csv('Lista_3/weather_2000.csv', usecols=colunas)
df.columns = ['DATA', 'HORA', 'TEMP']

def dia_mais_quente_ano(ano):
    query = f"SELECT DATA, MAX(TEMP) FROM df WHERE DATA LIKE '{ano}%'"
    resultado = sqldf(query)
    return resultado

def media_temperatura_ano(ano):
    query = f"SELECT AVG(TEMP) as media_temp FROM df WHERE DATA LIKE '{ano}%'"
    resultado = sqldf(query)
    return resultado

def media_janeiro_2010():
    query = "SELECT AVG(TEMP) as media_temp FROM df WHERE DATA LIKE '2010-01%'"
    resultado = sqldf(query)
    return resultado

def janeiro_2021_frio():
    query = "SELECT AVG(TEMP) as media_temp FROM df WHERE DATA LIKE '2021-01%'"
    resultado = sqldf(query)
    media = resultado['media_temp'][0]
    if media < 20:  # Assumindo que abaixo de 20°C é considerado frio
        return "Sim, fez frio."
    else:
        return "Não, não fez frio."

def compara_media_anos(ano1, ano2):
    media1 = media_temperatura_ano(ano1)['media_temp'][0]
    media2 = media_temperatura_ano(ano2)['media_temp'][0]
    if media1 > media2:
        return f"A média de {ano1} foi maior que a de {ano2}."
    elif media1 < media2:
        return f"A média de {ano2} foi maior que a de {ano1}."
    else:
        return f"As médias de {ano1} e {ano2} foram iguais."

# Testando as funções
print(dia_mais_quente_ano(2001))
print(dia_mais_quente_ano(2021))
print(media_temperatura_ano(2021))
print(media_janeiro_2010())
print(janeiro_2021_frio())
print(compara_media_anos(2001, 2021))
