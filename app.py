import tkinter as tk
from router_control import restart_router

def on_restart():
    ip = ip_entry.get()
    user = user_entry.get()
    pwd = pwd_entry.get()
    result = restart_router(ip, user, pwd)
    result_label.config(text=result)

window = tk.Tk()
window.title("Router Rebooter")
window.geometry("350x250")

tk.Label(window, text="Router IP:").pack(pady=2)
ip_entry = tk.Entry(window)
ip_entry.insert(0, "192.168.0.1")
ip_entry.pack(pady=2)

tk.Label(window, text="Username:").pack(pady=2)
user_entry = tk.Entry(window)
user_entry.insert(0, "admin")
user_entry.pack(pady=2)

tk.Label(window, text="Password:").pack(pady=2)
pwd_entry = tk.Entry(window, show="*")
pwd_entry.insert(0, "")
pwd_entry.pack(pady=2)

tk.Button(window, text="Restart Router", command=on_restart).pack(pady=10)
result_label = tk.Label(window, text="", fg="blue")
result_label.pack()

window.mainloop()
