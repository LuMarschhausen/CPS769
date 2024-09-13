from src.data_processing import load_data, merge_data
from src.qoe_calculation import apply_qoe_calculation
from src.function_calling import respond_to_question

def main():
    bitrate_data, rtt_data = load_data()
    merged_data = merge_data(bitrate_data, rtt_data)
    data_with_qoe = apply_qoe_calculation(merged_data)

    question = input("Qual a sua pergunta sobre a QoE?: ")
    response = respond_to_question(question, data_with_qoe)
    print(response)

if __name__ == "__main__":
    main()
