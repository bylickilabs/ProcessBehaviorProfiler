def detect_anomalies(df):
    anomalies = []
    for i, row in df.iterrows():
        if row['cpu_percent'] > 50 or row['memory_percent'] > 20:
            anomalies.append(i)
        elif "miner" in str(row['name']).lower() or "crypto" in str(row['name']).lower():
            anomalies.append(i)
    return anomalies
