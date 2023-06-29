import tkinter as tk
from tkinter import messagebox

class LineWindow(tk.Toplevel):
    def __init__(self, master=None, callback=None):
            super().__init__(master)
            self.callback = callback
            self.title("Détails de la ligne")
            
            # Création des champs de saisie pour la longueur de ligne, la distance entre les luminaires et la distance depuis l'armoire
            tk.Label(self, text="Longueur de ligne: ").grid(row=0)
            self.entry_length = tk.Entry(self)
            self.entry_length.grid(row=0, column=1)

            tk.Label(self, text="Distance entre les luminaire: ").grid(row=1)
            self.entry_width = tk.Entry(self)
            self.entry_width.grid(row=1, column=1)

            tk.Label(self, text="Distance sur laquelle les luminaires\nne seront pas posés (distance depuis l'armoire): ").grid(row=2)
            self.entry_distance = tk.Entry(self)
            self.entry_distance.grid(row=2, column=1)

            # Bouton de soumission qui appelle la fonction submit()
            tk.Button(self, text="Soumettre", command=self.submit).grid(row=3, columnspan=2)
        
    def submit(self):
        if self.callback:
            length = self.validate_input(self.entry_length.get())
            width = self.validate_input(self.entry_width.get())
            distance = self.validate_input_0(self.entry_distance.get())
            if length is not None and width is not None and distance is not None:
                self.callback(length, width, distance)
                self.destroy()

    @staticmethod
    def validate_input(input):
        try:
            val = float(input)
            if val > 0:
                return val
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre positif.")
                return None
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
            return None

    @staticmethod
    def validate_input_0(input):
        if input == "":
            return 0.0
        try:
            val = float(input)
            if val > 0:
                return val
            else:
                messagebox.showerror("Erreur", "Veuillez entrer un nombre positif.")
            return None
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
            return None

