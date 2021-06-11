| Samuel MANECHEZ | 11/06/2021 | TP-Puissance-4 |
| :--------------------------------------------------------------: | :--------: | :-------------------------------: |

# Puissance-4-python
Premier projet python

## P4_GUI
> P4_GUI est le projet initiale. Un puissance 4 avec interface graphique. J'ai passé beaucoup d'heures à essayer de le developper mais cela reste cependant au dessus de mes capacités actuelles. 

### Pre-requis
Télécharger le dossier P4_GUI ou la release.

### Utilisation
Installer les dépendances en vous plaçant dans le dossier des programmes ```.py``` et éxécutez la commande suivante:
```Python
pip install -r requirements.txt
```

Pour terminer lancer le programme ```main.py``` à l'aide de cette commande :
```Python
python3 main.py
```

![GUI interface](/P4_GUI/GUI.png)

## P4_CLI
> P4_CLI est le projet sur lequel je me suis rabbatu. Le programme est loin d'être parfait et ne gère pas les diagonales.

### Pre-requis
Télécharger le dossier P4_CLI ou la release.

### Utilisation
Installer les dépendances en vous plaçant dans le dossier des programmes ```.py``` et éxécutez la commande suivante:
```Python
pip install -r requirements.txt
```
Pour terminer lancer le programme ```main.py``` à l'aide de cette commande :
```Python
python3 main.py
```

### Règle du jeu
- Le plateau est représenté par un tableau avec des colonnes allant de 0 à 6. Vous devez saisir un entier compris entre 1 et 6. Le symbole sera automatiquement glissé dans la colonne.
- La vérification est uniquement horizontale et verticale.
- Il faut aligner 4 symboles aligné pour remporter la partie.
- Vous pouvez appuyer sur ```ctrl``` + ```z``` pour arrêter le programme.

Liste des symboles :
| Type de joueur | Symbole | 
| :--------: | :--------: |
| Humain | O |
| Ordinateur | x |

![CLI interface](/P4_CLI/CLI.png)
