from Atbasch import atbasch
import tkinter as tk

window = tk.Tk()
window.title("Crypt")
window.configure(padx = 5, pady = 5)

textin_var = tk.StringVar()

def submit():
    textin = textin_var.get()
    textout = atbasch(textin)
    
    label_tout.config(state = tk.NORMAL)
    label_tout.delete(0, tk.END)
    label_tout.insert(0, textout)
    label_tout.config(state = tk.DISABLED)

def copy():
    text=label_tout.get()
    window.clipboard_clear()
    window.clipboard_append(text)
   
label_tin = tk.Label(window, text = "Text Eingeben:")
label_tin.grid(row = 0, column = 0)

textin = tk.Entry(window, textvariable = textin_var)
textin.grid(row = 0, column = 1)

button_sub = tk.Button(window, text = "Ver-/Entschlüsseln", command = submit)
button_sub.grid(row = 1, column = 0, columnspan = 2, pady = 5)

label_l_tout = tk.Label(window, text = "Ausgabe:")
label_l_tout.grid(row = 2, column = 0, pady = 5, sticky = "w")

label_tout = tk.Entry(window)
label_tout.insert(0,"")
label_tout.config(state = tk.DISABLED)
label_tout.grid(row = 2, column = 1, pady = 5, sticky = "nesw")

button_copy = tk.Button(window, text = "Kopieren", command = copy)
button_copy.grid(row = 2, column = 2)

window.mainloop()
