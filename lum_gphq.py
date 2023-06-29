import tkinter as tk
import math as mt
from tkinter import messagebox

class LineWindow(tk.Toplevel):
    def __init__(self, master=None, callback=None):
        super().__init__(master)
        self.callback = callback
        self.title("Détails de la ligne")
        
        tk.Label(self, text="Longueur de ligne: ").grid(row=0)
        self.entry_length = tk.Entry(self)
        self.entry_length.grid(row=0, column=1)

        tk.Label(self, text="Distance entre les luminaire: ").grid(row=1)
        self.entry_width = tk.Entry(self)
        self.entry_width.grid(row=1, column=1)

        tk.Label(self, text="Distance sur laquelle les luminaires\nne seront pas posés (distance depuis l'armoire): ").grid(row=2)
        self.entry_distance = tk.Entry(self)
        self.entry_distance.grid(row=2, column=1)

        tk.Button(self, text="Soumettre", command=self.submit).grid(row=3, columnspan=2)
    
    def submit(self):
        if self.callback:
            if validate_input(self.entry_length.get()) and validate_input(self.entry_width.get()) and validate_input(self.entry_distance.get()):
                self.callback(float(self.entry_length.get()), float(self.entry_width.get()), float(self.entry_distance.get()))
                self.destroy()

def validate_input(input):
    try:
        val = float(input)
        if val > 0:
            return True
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre positif.")
            return False
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        return False

def n_light(lenght, widht, w):
    n = (lenght-w)/widht
    n = mt.ceil(n)
    wire = [w + widht * i for i in range(n)]
    l = sum(wire)
    return l, n

def calculate():
    total_cable_length = sum(line[3][0] for line in lines)
    total_luminaires = sum(line[3][1] for line in lines)
    label_cable["text"] = "Longueur totale de câble pour les luminaires : " + str(total_cable_length) + " m"
    label_luminaire["text"] = "Nombre total de luminaires : " + str(total_luminaires)

def add_line():
    LineWindow(root, callback=update_line)

def update_line(lenght, widht, w):
    line = n_light(lenght, widht, w)
    lines.append([lenght, widht, w, line])
    summary_text = f"Pour la ligne {len(lines)} :\nLongueur de ligne : {lenght} m, Espacement entre les luminaires : {widht} m, Distance sur laquelle les luminaires ne sont pas posés : {w} m\nLongueur du câble : {line[0]} m, Nombre de luminaires : {line[1]}"
    summaries.append(tk.Label(root, text=summary_text))
    summaries[-1].grid(row=len(lines)+4, columnspan=2)


root = tk.Tk()
root.title("Calculateur de luminaires et de câbles")

lines = []
summaries = []

tk.Button(root, text="Ajouter une ligne", command=add_line).grid(row=0, column=0)
tk.Button(root, text="Fin", command=calculate).grid(row=0, column=1)

label_cable = tk.Label(root, text="")
label_cable.grid(row=2, column=0, columnspan=2)
label_luminaire = tk.Label(root, text="")
label_luminaire.grid(row=3, column=0, columnspan=2)

root.mainloop()
