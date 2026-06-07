import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://sandipbgt.com/theastrologer/api/"

def get_signs():
    try: 
        return requests.get(f"{API_URL}/sunsigns/").json()
    except:
        messagebox.showerror("Crystal Ball Error", "Could not fetch star sign")
        return []
    
    
def get_horoscope():
    user_sign = selected_sign.get().lower()
    
    if not user_sign:
        messagebox.showwarning("Missing sign", "Please choose star sign")
        return

    try:
        horoscope_json = requests.get(f"{API_URL}/horoscope/{user_sign}/today").json()
    
        horoscope_text.config(state="normal")
        horoscope_text.delete("1.0", tk.END)
        horoscope_text.insert(tk.END, horoscope_json["horoscope"])
        horoscope_text.config(state="disabled")
        
    except:
        messagebox.showerror("Cosmic Error", "Could not fetch your horroscope.")
    

root = tk.Tk()
root.title("Daily Horoscope")
root.geometry("600x500")
root.configure(bg="#1b0033")

title = tk.Label(
    root,
    text="Daily Horoscope",
    font=("Georgia", 28, "bold"),
    fg="#ffd700",
    bg="#1b0033"
)
title.pack(pady=25)

subtitle = tk.Label(
    root,
    text="Choose your star sign and reveal today's cosmic message",
    font=("Georgia", 13),
    fg="#e0b3ff",
    bg="#1b0033"
)
subtitle.pack(pady=5)

signs = get_signs()
selected_sign = tk.StringVar()

dropdown = tk.OptionMenu(root, selected_sign, *[sign.title() for sign in signs])
dropdown.config(
    font=("Georgia", 14),
    bg="#6a0dad",
    fg="white",
    activebackground="#9b30ff",
    activeforeground="white",
    width=20
)

dropdown["menu"].config(
    bg="#2d004d",
    fg="white",
    font=("Georgia", 12)
)
dropdown.pack(pady=25)

button = tk.Button(
    root,
    text="✨ Reveal My Horoscope ✨",
    command=get_horoscope,
    font=("Georgia", 14, "bold"),
    bg="#ff69b4",
    fg="white",
    activebackground="#ffd700",
    activeforeground="#1b0033",
    padx=20,
    pady=10,
    relief="raised",
    bd=4
)
button.pack(pady=10)

horoscope_frame = tk.Frame(root, bg="#ffd700", padx=3, pady=3)
horoscope_frame.pack(pady=25)

horoscope_text = tk.Text(
    horoscope_frame,
    width=55,
    height=10,
    wrap="word",
    font=("Georgia", 12),
    bg="#2d004d",
    fg="#fff5cc",
    padx=15,
    pady=15,
    relief="flat"
)
horoscope_text.pack()
horoscope_text.insert(tk.END, "Your horoscope will appear here...")
horoscope_text.config(state="disabled")

footer = tk.Label(
    root,
    text="☽ Written in the stars ☾",
    font=("Georgia", 11, "italic"),
    fg="#c084fc",
    bg="#1b0033"
)
footer.pack(pady=10)

root.mainloop()

"""
signs = requests.get("http://sandipbgt.com/theastrologer/api/sunsigns/").json()
user_sign = ""

print("** STAR SIGNS **")
for sign in signs:
    print(f"  - {sign.title()}")
    
while user_sign not in signs:
    user_sign = input("Please select your star sign: ").lower()
    
horoscope_json = requests.get(f"http://sandipbgt.com/theastrologer/api/horoscope/{user_sign}/today").json()

print(horoscope_json["horoscope"])
"""