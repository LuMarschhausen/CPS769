def calculate_qoe(row):
    if row['rtt'] == 0:
        return row['bitrate'] / 0.0001
    return row['bitrate'] / row['rtt']

def apply_qoe_calculation(merged_data):
    merged_data['QoE'] = merged_data.apply(calculate_qoe, axis=1)
    return merged_data
