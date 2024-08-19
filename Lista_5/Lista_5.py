import PyPDF2
import openai
import numpy as np

# Configuração da API da OpenAI
openai.api_key = "sua-chave-api-aqui"

# Função para carregar e processar o artigo
def carregar_artigo(caminho):
    with open(caminho, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        texto = ''
        for page in range(len(reader.pages)):
            texto += reader.pages[page].extract_text()
    return texto

# Função para gerar embeddings usando a nova API da OpenAI
def gerar_embeddings(texto):
    response = openai.Embedding.create(
        input=texto,
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return np.array(embeddings)

# Função para processar as perguntas e gerar respostas
def responder_perguntas(artigo, pergunta):
    artigo_emb = gerar_embeddings(artigo)
    pergunta_emb = gerar_embeddings(pergunta)
    
    # Calcular similaridade entre a pergunta e as partes do artigo
    similaridade = np.dot(artigo_emb, pergunta_emb.T)
    indice_mais_similar = np.argmax(similaridade)
    
    # Gerar resposta usando a API da OpenAI com base na parte mais similar do artigo
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=artigo[indice_mais_similar],
        max_tokens=150
    )
    
    return resposta.choices[0].text.strip()

# Interface simples para receber perguntas do usuário
def interface_usuario(caminho_artigo):
    artigo = carregar_artigo(caminho_artigo)
    
    while True:
        pergunta = input("Digite sua pergunta: ")
        if pergunta.lower() == "sair":
            break
        resposta = responder_perguntas(artigo, pergunta)
        print(f"Resposta: {resposta}\n")

# Main
if __name__ == "__main__":
    caminho_artigo = r"C:\Users\Luisa\Desktop\CPS769\CPS769\Lista_5\524_icmlpaper.pdf"  # Caminho absoluto para o arquivo PDF
    interface_usuario(caminho_artigo)
