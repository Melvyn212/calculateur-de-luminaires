import math as mt

#parametres

espacement=10

def n_light (lenght,widht,w):# lenght= distance de l'amoire au luminaire le plus loin; widht = espacement entre les luminaire ; w=longueur contenant deja des luminaires
  n=(lenght-w)/widht # calcul le nombre de luminaires pour une zone qui n'en contien pas
  n=mt.ceil(n)
  wire=[]
  for i in range(int(n)):
    w=w+widht
    wire.append(w)
  l=sum(wire)
  return l,n

def ask_data_int():
    while True:
        try:
            nombre = int(input("Entrez un nombre de ligne : "))
            if nombre <= 0:  # Ajout de la condition de positivité
                print("Erreur : Veuillez entrer un nombre entier positif.")
            else:
                break  # Sort de la boucle si un entier valide est saisi
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
    return nombre

def ask_data_float():
    while True:
        try:
            nombre = float(input("Entrez la mesure : "))
            if nombre <= 0:  # Ajout de la condition de positivité
                print("Erreur : Veuillez entrer un nombre positif.")
            else:
                break  # Sort de la boucle si un nombre valide est saisi
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")
    return nombre

cable = {}
luminaire = {}
for i in range(ask_data_int()):
  print("\nLigne09 ",i+1,"\n\n")
  nom_variablea = "a" + str(i)
  nom_variableb = "b" + str(i)
  print("longueur de ligne\n")
  lenght=ask_data_float()
  print("\nok")
  print("\ndistance entre les luminaire\n")
  widht=ask_data_float()
  print("\nok")
  print("\ndistance sur laquelle les luminaires\n ne seront pas posée(distance depuis l'armoire)\n")
  w=ask_data_float()
  print("\nok")
  cable[nom_variablea],luminaire[nom_variableb] = n_light(lenght,widht,w)

print(cable)
print(luminaire)

print("la longueur total de cable pour les luminaires:",sum(cable.values()), "m")
print("\nle nombre total de luminaires : ", sum(luminaire.values()))