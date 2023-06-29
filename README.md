Pour lum_gphq.py

Le code que nous avons écrit peut être visualisé en tant que "Grafcet" ou diagramme de flux comme suit :

1. Initialisation de l'application :
   - Créer une fenêtre principale.
   - Ajouter des boutons "Ajouter une ligne" et "Fin" à la fenêtre principale.
   - Initialiser une liste vide `lines` pour stocker les informations des lignes.

2. Lorsque l'utilisateur clique sur le bouton "Ajouter une ligne" :
   - Une nouvelle fenêtre `LineWindow` s'ouvre.
   - L'utilisateur peut saisir les détails de la ligne : longueur, espacement entre les luminaires et distance sur laquelle les luminaires ne sont pas posés.
   - Lorsque l'utilisateur soumet les détails, les informations sont validées. Si les informations sont correctes, elles sont renvoyées à la fenêtre principale et la fenêtre `LineWindow` est fermée. Si les informations sont incorrectes, un message d'erreur s'affiche.

3. Lorsque les détails de la ligne sont renvoyés à la fenêtre principale :
   - La fonction `n_light` calcule la longueur du câble et le nombre de luminaires pour la ligne.
   - Les détails de la ligne et les résultats des calculs sont ajoutés à la liste `lines`.
   - Un résumé des détails et des résultats de la ligne est ajouté à la fenêtre principale.

4. L'utilisateur peut ajouter autant de lignes qu'il le souhaite en répétant les étapes 2 et 3.

5. Lorsque l'utilisateur a fini d'ajouter des lignes et clique sur le bouton "Fin" :
   - La fonction `calculate_total` calcule la longueur totale du câble et le nombre total de luminaires à partir des informations de toutes les lignes dans la liste `lines`.
   - Ces totaux sont affichés dans la fenêtre principale.

6. L'application reste ouverte jusqu'à ce que l'utilisateur la ferme. 

Cela représente un flux de travail typique pour l'application. N'hésitez pas à poser d'autres questions si vous avez besoin de plus de détails ou d'éclaircissements sur des parties spécifiques du code ou du flux de travail.
