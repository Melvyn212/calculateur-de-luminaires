import math as mt
import tkinter as tk
from line_window import LineWindow
from tkinter import ttk
from ttkthemes import ThemedTk


class LineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculateur de luminaires et de câbles")
        self.lines = []
        self.summaries = []
                # Define a style for the buttons
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), background="black", foreground="white")
        style.configure("TLabel", font=("Helvetica", 12))

        tk.Button(self.root, text="Ajouter une ligne", command=self.add_line).grid(row=0, column=0)
        tk.Button(self.root, text="Total", command=self.calculate).grid(row=0, column=1)
        self.label_cable = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), fg="red")
        self.label_cable.grid(row=2, column=0, columnspan=2)
        self.label_luminaire = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), fg="red")
        self.label_luminaire.grid(row=3, column=0, columnspan=2)

    def add_line(self):
        LineWindow(self.root, callback=self.update_line)

    def update_line(self, lenght, widht, w):
        line = self.n_light(lenght, widht, w)
        self.lines.append([lenght, widht, w, line])
        summary_text = f"Pour la ligne {len(self.lines)} :\nLongueur de ligne : {lenght} m, Espacement entre les luminaires : {widht} m, Distance sur laquelle les luminaires ne sont pas posés : {w} m\nLongueur du câble : {line[0]} m, Nombre de luminaires : {line[1]}"
        self.summaries.append(tk.Label(self.root, text=summary_text))
        self.summaries[-1].grid(row=len(self.lines)+4, columnspan=2)

    def calculate(self):
        total_cable_length = sum(line[3][0] for line in self.lines)
        total_luminaires = sum(line[3][1] for line in self.lines)
        self.label_cable["text"] = "Longueur totale de câble pour les luminaires : " + str(total_cable_length) + " m"
        self.label_luminaire["text"] = "Nombre total de luminaires : " + str(total_luminaires)

    @staticmethod
    def n_light(lenght, widht, w):
        n = (lenght-w)/widht
        n = mt.ceil(n)
        wire = [w + widht * i for i in range(n)]
        l = sum(wire)
        return l, n
