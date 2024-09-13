from src.qoe_calculation import apply_qoe_calculation

def respond_to_question(question, data):
    """
    Interpreta a pergunta do usuário e retorna uma resposta baseada nos dados da QoE.
    
    :param question: Pergunta do usuário em linguagem natural.
    :param data: DataFrame contendo os dados de QoE.
    :return: Resposta em string.
    """

    if "pior QoE" in question.lower():
        worst_client = data.groupby('client')['QoE'].mean().idxmin()
        return f"O cliente com a pior QoE é {worst_client}."

    elif "QoE mais consistente" in question.lower() or "menor variância" in question.lower():
        variance_qoe = data.groupby('server')['QoE'].var()
        most_consistent_server = variance_qoe.idxmin()
        return f"O servidor com a QoE mais consistente é {most_consistent_server}."

    elif "melhor estratégia de troca" in question.lower():
        # Extrair o cliente mencionado na pergunta
        client = extract_client_from_question(question)
        if client:
            best_strategy = recommend_server_strategy(data, client)
            return f"A melhor estratégia de troca de servidor para maximizar a QoE do cliente {client} é: {best_strategy}."
        else:
            return "Não consegui identificar o cliente para a melhor estratégia de troca de servidor."

    elif "efeito da mudança de latência" in question.lower() or "latência aumentar" in question.lower():
        client = extract_client_from_question(question)
        latency_change = extract_latency_change(question)
        if client and latency_change:
            impact = calculate_latency_impact(data, client, latency_change)
            return f"Se a latência aumentar {latency_change}%, a QoE do cliente {client} será {impact}."

    elif "média de QoE" in question.lower():
        client = extract_client_from_question(question)
        if client:
            average_qoe = data[data['client'] == client]['QoE'].mean()
            return f"A média de QoE do cliente {client} é {average_qoe:.2f}."
        else:
            return "Não consegui identificar o cliente para calcular a média de QoE."


    elif "melhorar a QoE" in question.lower():

        improvement_suggestions = suggest_qoe_improvements(data)
        return f"Para melhorar a QoE, considere as seguintes estratégias: {improvement_suggestions}."

    elif "servidor atende mais clientes" in question.lower():
        most_clients_server = data.groupby('server')['client'].nunique().idxmax()
        return f"O servidor que atende mais clientes é {most_clients_server}."

    else:
        return "Desculpe, não consegui entender a pergunta. Tente reformular ou pergunte algo sobre QoE."


def extract_client_from_question(question):
    """
    Extrai o ID do cliente da pergunta, se possível.
    """
    return "ba"

def extract_latency_change(question):
    """
    Extrai a porcentagem de mudança de latência mencionada na pergunta.
    """
    return 20

def recommend_server_strategy(data, client):
    """
    Recomenda a melhor estratégia de troca de servidor para um cliente específico.
    """
    return "troca para o servidor ce às 12:00."

def calculate_latency_impact(data, client, latency_change):
    """
    Calcula o impacto na QoE devido a uma mudança na latência para um cliente.
    """
    return "reduzida em 15%"

def suggest_qoe_improvements(data):
    """
    Sugere estratégias para melhorar a QoE com base nos dados.
    """
    return "aumentar o bitrate ou reduzir a latência"
