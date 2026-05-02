# Puissance 4

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame&logoColor=white)

> Jeu de **Puissance 4** en Python avec interface graphique pygame.
> Le joueur affronte l'ordinateur ou un second joueur en local.

---

## Table des matières

- [Démarrer le programme](#démarrer-le-programme)
- [Comment jouer](#comment-jouer)
- [Structure du projet](#structure-du-projet)
- [Fonctions moteur](#fonctions-moteur--enginepy)
- [Fonctions d'affichage](#fonctions-daffichage--displaypy)
- [Boucle principale](#boucle-principale--puissance4py)
- [Assets](#assets--assetspy)

---

## Démarrer le programme

### Lancement

```
puissance4.py
```

---

## Comment jouer

1. **Menu principal** - Cliquer sur *Nouvelle partie* pour lancer une partie, ou *Quitter* pour fermer.
2. **Choisir le mode** - Sélectionner *1 PLAYER* pour affronter le bot, ou *2 PLAYER* pour jouer à deux en local.
3. **Jouer un jeton** - Déplacer la souris sur la colonne souhaitée et cliquer. Le jeton tombe automatiquement.
4. **Gagner** - Aligner 4 jetons de sa couleur horizontalement, verticalement ou en diagonale.
5. **Fin de partie** - Un écran affiche le vainqueur. Cliquer pour rejouer ou fermer la fenêtre pour quitter.

> **Joueur 1** = rouge · **Joueur 2 / Bot** = jaune

---

## Structure du projet

```
└── Projets/
    └── Jeux/Puissance4/
        ├── Back/
        │   └── engine.py                  # Logique de jeu et IA minimax
        ├── Front/
        │   ├── assets.py                  # Chargement des ressources graphiques
        │   └── display.py                 # Fonctions d'affichage pygame
        └── puissance4.py              # Point d'entrée, boucle principale
```

---

## Fonctions moteur : `engine.py`

| Fonction                            | Retour   | Description                                                                                                                |
|-------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------|
| `free_column_verif(column, grid)`   | `bool`   | Vérifie si la colonne est disponible (case du haut vide)                                                                   |
| `free_row(column, grid)`            | `int`    | Retourne l'index de la première ligne occupée dans la colonne, ou `len(grid)-1` si elle est entièrement libre              |
| `verification(grid)`                | `tuple`  | Vérifie l'état de la grille. Retourne `(True, 1)` ou `(True, 2)` si victoire, `(True, 0)` si égalité ou `(False, 0)` sinon |
| `play(grid, ligne, column, joueur)` | `None`   | Place un jeton dans la grille à la position donnée                                                                         |
| `bot_choice(grid)`                  | `int`    | Calcule le meilleur coup pour le bot via l'algorithme minimax (IA)                                                         |

---

## Fonctions d'affichage : `display.py`

| Fonction                                                | Retour  | Description                                                              |
|---------------------------------------------------------|---------|--------------------------------------------------------------------------|
| `mode()`                                                | `int`   | Affiche le choix du mode. `1` = solo vs bot, `2` = 2 joueurs             |
| `choice(grid, turn)`                                    | `int`   | Attend le clic du joueur sur une colonne. Retourne l'index de la colonne |
| `drop(color, col, grid, free_rows)`                     | `None`  | Anime la chute du jeton dans la colonne                                  |
| `game_over(winner, grid)`                               | `bool`  | Affiche l'écran de fin. `True` = rejouer, `False` = quitter              |
| `display_chips(grid)`                                   | `None`  | Redessine tous les jetons et la grille à partir de l'état de `grid`      |
| `affichage_menu(p1, p2)`                                | `None`  | Affiche les boutons de sélection du mode                                 |
| `fondu()`                                               | `None`  | Petite animation de fondu d'ouverture                                    |

### Constantes globales

| Variable  | Valeur                 | Description                                                  |
|-----------|------------------------|--------------------------------------------------------------|
| `columns` | `[105, 205, ..., 705]` | Coordonnées X des 7 colonnes (espacement de 100 px)          |
| `rows`    | `[154, 254, ..., 654]` | Coordonnées Y des 6 lignes (espacement de 100 px)            |

---

## Boucle principale : `puissance4.py`

### Schéma de la boucle

```
fondu()
└── while main_menu()
    ├── mode()                        ← choix du mode (solo ou duo)
    └── while True
        ├── choice()                  ← joueur 1 choisit sa colonne
        ├── bot_choice() ou choice()  ← joueur 2 ou bot choisit
        ├── drop()                    ← animation de la chute
        └── verification()            ← détection victoire / égalité
            └── game_over()           ← écran de fin
```

---

## Assets : `assets.py`

### `load_assets()`

Charge toutes les ressources graphiques depuis le dossier `Assets/` :

| Variable retournée | Description                                              |
|--------------------|----------------------------------------------------------|
| `chips`            | Liste `[red, yellow]` - images des jetons rouge et jaune |
| `grid_img`         | Image de la grille de jeu                                |
