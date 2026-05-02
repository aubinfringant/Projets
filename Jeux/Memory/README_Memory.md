# Memory

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame&logoColor=white)

> Jeu de **Memory** en Python avec interface graphique pygame.
> Le joueur retourne des cartes deux par deux pour trouver toutes les paires.

---

## Table des matières

- [Démarrer le programme](#démarrer-le-programme)
- [Comment jouer](#comment-jouer)
- [Structure du projet](#structure-du-projet)
- [Classe Grid](#classe-grid--gridmemorypy)
- [Fonctions d'affichage](#fonctions-daffichage--displaypy)
- [Boucle principale](#boucle-principale--memorypy)
- [Assets](#assets--assetspy)

---

## Démarrer le jeu

### Lancement

```
memory.py
```

---

## Comment jouer

1. **Menu principal** - Cliquer sur *Nouvelle partie* pour lancer une partie, ou *Quitter* pour fermer.
2. **Retourner une carte** - Cliquer sur une carte face cachée pour la révéler.
3. **Retourner une seconde carte** - Cliquer sur une autre carte. Si les deux cartes sont identiques, elles restent visibles.
4. **Continuer** - Si les deux cartes sont différentes, cliquer n'importe où pour les retourner face cachée et passer au tour suivant.
5. **Fin de partie** - Lorsque toutes les paires sont trouvées, le menu principal s'affiche pour rejouer.

---

## Structure du projet

```
└── Projets/
    ├── Class/
    │   ├── Deck52.py                      # Classes Card et Deck
    │   └── GridMemory.py                  # Classe Grid
    └── Jeux/Memory/
             ├── Front/   
             │   ├── assets.py                  # Chargement des ressources graphiques
             │   └── display.py                 # Fonctions d'affichage pygame
             └── memory.py                      # Point d'entrée, boucle principale
```

---

## Classe Grid : `GridMemory.py`

Représente la grille de jeu contenant les cartes.

| Attribut    | Type               | Description                                                              |
|-------------|--------------------|--------------------------------------------------------------------------|
| `paires`    | `int`              | Nombre de paires à trouver (`width × height // 2`)                       |
| `grid`      | `list[list[Card]]` | Grille 2D contenant les objets `Card`                                    |
| `bool_grid` | `list[list[bool]]` | Grille 2D miroir : `False` = carte non trouvée, `True` = paire trouvée   |

| Méthode           | Retour             | Description                                                              |
|-------------------|--------------------|--------------------------------------------------------------------------|
| `add_card()`      | `None`             | Pioche `paires` cartes uniques, les duplique, mélange et remplit `grid`  |
| `find_card(card)` | `None`             | Met à `True` dans `bool_grid` toutes les cases contenant la carte donnée |
| `full()`          | `bool`             | Retourne `True` si toutes les cases de `bool_grid` valent `True`         |

---

## Fonctions d'affichage : `display.py`

| Fonction                                                | Retour  | Description                                                                                                       |
|---------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------|
| `card_choice(grid, found_cards, choices)`               | `tuple` | Gère la sélection d'une carte. Retourne `(card, cord)` au clic sur une carte valide. Retourne `None` si fermeture |
| `display_cards(grid, grid_colid, found_cards, choices)` | `None`  | Redessine toutes les cartes : face visible pour les paires trouvées et les choix en cours, dos pour les autres    |
| `confirmation(grid, found_cards, choices)`              | `None`  | Fait une pause pour bien mémoriser les deux cartes différentes                                                    |

---

## Boucle principale : `memory.py`

### Schéma de la boucle

```
main_menu()
└── while run
    ├── Grid(4, 4) + add_card()          ← nouvelle grille de 16 cartes (8 paires)
    └── while grid.full()                ← tant qu'il manque une paire
        ├── card_choice()                ← 1er choix du joueur
        ├── card_choice()                ← 2e choix du joueur
        ├── comparaison des deux choix
        │   └── si paire trouvée → find_card() + found_cards
        └── confirmation()               ← affichage des deux cartes, attente d'un clic
```

---

## Assets : `assets.py`

### `load_assets()`

Charge toutes les ressources graphiques depuis le dossier `Assets/` :

| Variable retournée | Type        | Description                                     |
|--------------------|-------------|-------------------------------------------------|
| `card_back`        | `Surface`   | Image du dos de carte                           |
| `cards_sprite`     | `dict`      | Dictionnaire `(valeur, couleur)` → image pygame |
| `carpet`           | `Surface`   | Image de fond du tapis de jeu                   |