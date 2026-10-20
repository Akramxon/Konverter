import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Valyuta konvertori")
tk.Label(root, text="Valyuta konvertori", font=("Arial", 20)).pack()
tk.Label(root, text="FROM").pack()

manba = ttk.Combobox(root, values=["UZS", "USD", "EUR"], state="readonly")
manba.set("UZS")
manba.pack()

tk.Label(root, text="TO").pack()

maqsad = ttk.Combobox(root, values=["UZS", "USD", "EUR"], state="readonly")
maqsad.set("USD")
maqsad.pack()
miqdor = tk.Entry(root)
miqdor.pack()
natija= tk.Label(root, text="Natija (dollar):")
natija.pack()
def konvert():
    summa = float(miqdor.get())

    kurslar = {
        "UZS": 1,
        "USD": 12000,
        "EUR": 13900
    }

    som = summa * kurslar[manba.get()]
    hisob = som / kurslar[maqsad.get()]

    natija.config(text=f"Natija: {hisob:.2f} {maqsad.get()}")


    
button=tk.Button(root, text="Konvert qilish", command=lambda: konvert())
button.pack()
root.geometry('310x340')
root.resizable(height=False , width=False)

root.mainloop() 
