

# Création d'une classe pour une nouvelle fenêtre pour entrer les détails de la ligne
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
        # Cette fonction récupère les valeurs saisies et les valide. Si elles sont valides, elles sont transmises à la fonction de rappel
        if self.callback:
            length = validate_input(self.entry_length.get())
            width = validate_input(self.entry_width.get())
            distance = validate_input_0(self.entry_distance.get())
            if length is not None and width is not None and distance is not None:
                self.callback(length, width, distance)
                self.destroy()

# Fonctions pour valider les entrées. Les entrées doivent être des nombres positifs
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

# Fonction pour valider les entrées qui peuvent être zéro
def validate_input_0(input):
    if input == "":
        return 0.0
    try:
        val = float(input)
        if val >= 0:
            return val
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre positif.")
            return None
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide.")
        return None

# Fonction pour calculer le nombre de luminaires et la longueur du câble
def n_light(lenght, widht, w):
    n = (lenght-w)/widht
    n = mt.ceil(n)
    wire = [w + widht * i for i in range(n)]
    l = sum(wire)
    return l, n

# Fonction pour calculer les totaux pour toutes les lignes
def calculate():
    total_cable_length = sum(line[3][0] for line in lines)
    total_luminaires = sum(line[3][1] for line in lines)
    label_cable["text"] = "Longueur totale de câble pour les luminaires : " + str(total_cable_length) + " m"
    label_luminaire["text"] = "Nombre total de luminaires : " + str(total_luminaires)

# Fonction pour ouvrir une nouvelle fenêtre LineWindow
def add_line():
    LineWindow(root, callback=update_line)

# Fonction pour ajouter une ligne et mettre à jour l'interface utilisateur
def update_line(lenght, widht, w):
    line = n_light(lenght, widht, w)
    lines.append([lenght, widht, w, line])
    summary_text = f"Pour la ligne {len(lines)} :\nLongueur de ligne : {lenght} m, Espacement entre les luminaires : {widht} m, Distance sur laquelle les luminaires ne sont pas posés : {w} m\nLongueur du câble : {line[0]} m, Nombre de luminaires : {line[1]}"
    summaries.append(tk.Label(root, text=summary_text))
    summaries[-1].grid(row=len(lines)+4, columnspan=2)

# Création de l'interface utilisateur principale
root = tk.Tk()
root.title("Calculateur de luminaires et de câbles")

lines = []
summaries = []

# Boutons pour ajouter une ligne et calculer les totaux
tk.Button(root, text="Ajouter une ligne", command=add_line).grid(row=0, column=0)
tk.Button(root, text="Total", command=calculate).grid(row=0, column=1)

# Étiquettes pour afficher les totaux
label_cable = tk.Label(root, text="", font=("Helvetica", 12, "bold"), fg="red")
label_cable.grid(row=2, column=0, columnspan=2)
label_luminaire = tk.Label(root, text="", font=("Helvetica", 12, "bold"), fg="red")
label_luminaire.grid(row=3, column=0, columnspan=2)

# Lancement de l'interface utilisateur principale
root.mainloop()
