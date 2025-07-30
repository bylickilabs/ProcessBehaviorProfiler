import psutil
import pandas as pd
import time

def collect_process_data():
    data = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'username', 'create_time']):
        try:
            info = proc.info
            data.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return pd.DataFrame(data)

def get_timestamped_snapshot():
    df = collect_process_data()
    df['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
    return df
