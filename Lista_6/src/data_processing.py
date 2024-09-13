import pandas as pd

def load_data():
    bitrate_data = pd.read_excel('../data/bitrate_train.xlsx')
    rtt_data = pd.read_excel('../data/rtt_train.xlsx')
    return bitrate_data, rtt_data

def merge_data(bitrate_data, rtt_data):
    merged_data = pd.merge(bitrate_data, rtt_data, on=['client', 'server', 'timestamp'], how='inner')
    merged_data['rtt'] = pd.to_numeric(merged_data['rtt'], errors='coerce')
    return merged_data
