import tkinter as tk
from tkinter import messagebox
from detector import detect_url

def check_url():
    url = entry.get()
    result = detect_url(url)
    messagebox.showinfo("PhishGuardian Result", result)

root = tk.Tk()
root.title("🛡️ PhishGuardian - URL Scanner")
root.geometry("500x300")
root.config(bg="#1e1e2f")  # Dark Background
root.iconbitmap("logo.ico")  # App icon

heading = tk.Label(root, text="PhishGuardian", font=("Helvetica", 22, "bold"), fg="#00ffcc", bg="#1e1e2f")
heading.pack(pady=15)

sub = tk.Label(root, text="Enter any URL to check if it's safe", font=("Arial", 12), fg="#cccccc", bg="#1e1e2f")
sub.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12), width=40, bg="#2c2c3a", fg="white", insertbackground="white", borderwidth=2)
entry.pack(pady=10)

button = tk.Button(root, text="Check URL", font=("Arial", 12, "bold"), bg="#00ffcc", fg="black", command=check_url, padx=10, pady=5)
button.pack(pady=15)

footer = tk.Label(root, text="Powered by Mr. Manish 💻", font=("Arial", 9), fg="#666666", bg="#1e1e2f")
footer.pack(side="bottom", pady=10)

root.mainloop()
