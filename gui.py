import tkinter as tk
from tkinter import ttk
import threading
import time
from monitor import get_timestamped_snapshot
from detector import detect_anomalies

def launch_gui():
    root = tk.Tk()
    root.title("🔐 Process Behavior Profiler")

    tree = ttk.Treeview(root)
    tree["columns"] = ("PID", "Name", "CPU%", "RAM%", "User", "Startzeit", "Zeit")
    tree["show"] = "headings"
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)
    tree.pack(expand=True, fill="both")

    def update():
        while True:
            df = get_timestamped_snapshot()
            anomalies = detect_anomalies(df)
            for item in tree.get_children():
                tree.delete(item)
            for idx, row in df.iterrows():
                values = (row["pid"], row["name"], f'{row["cpu_percent"]:.1f}', f'{row["memory_percent"]:.1f}',
                          row["username"], time.strftime('%H:%M:%S', time.localtime(row["create_time"])), row["timestamp"])
                tags = ("anomaly",) if idx in anomalies else ()
                tree.insert("", "end", values=values, tags=tags)
            tree.tag_configure("anomaly", background="#ffcdd2")
            time.sleep(5)

    threading.Thread(target=update, daemon=True).start()
    root.mainloop()
