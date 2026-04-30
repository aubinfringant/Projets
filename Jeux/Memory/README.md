# Memory

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

> Jeu de **Memory** en Python avec interface graphique pygame.  
> Le joueur retourne des cartes deux par deux pour trouver toutes les paires.

---

## Table des matières

- [Démarrer le programme](#-démarrer-le-programme)
- [Comment jouer](#-comment-jouer)
- [Structure du projet](#-structure-du-projet)
- [Classe Grid](#-classe-grid--gridpy)
- [Fonctions d'affichage](#-fonctions-daffichage--displaypy)
- [Boucle principale](#-boucle-principale--memorypy)
- [Assets](#-assets--assetspy)

---

## Démarrer le programme

### Dépendances

**Bibliothèques standard** *(incluses avec Python, aucune installation nécessaire)* :

| Module | Utilisation |
|--------|-------------|
| `os` | Construction des chemins vers les assets graphiques |
| `random` | Mélange des cartes et tirage aléatoire pour remplir la grille |

**Bibliothèques à installer** :

```bash
pip install pygame
```

| Module | Utilisation |
|--------|-------------|
| `pygame` | Affichage, gestion des événements clavier/souris et chargement des images |

### Lancement

```bash
python memory.py
```

---

## Comment jouer

1. **Menu principal** — Cliquer sur *Nouvelle partie* pour lancer une partie, ou *Quitter* pour fermer.
2. **Retourner une carte** — Cliquer sur une carte face cachée pour la révéler.
3. **Retourner une seconde carte** — Cliquer sur une autre carte. Si les deux cartes sont identiques, elles restent visibles.
4. **Continuer** — Si les deux cartes sont différentes, cliquer n'importe où pour les retourner face cachée et passer au tour suivant.
5. **Fin de partie** — Lorsque toutes les paires sont trouvées, le menu principal s'affiche pour rejouer.

---

## Structure du projet

```
├── memory.py                              # Point d'entrée, boucle principale
└── Library/
    ├── Class/
    │   └── Deck_52.py                     # Classes Card et Deck
    └── Jeux/Memory/
        ├── Class/
        │   └── Grid.py                    # Classe Grid
        └── Front/
            ├── display.py                 # Fonctions d'affichage pygame
            └── assets.py                  # Chargement des ressources graphiques
```

---

## Classe Grid : `Grid.py`

Représente la grille de jeu contenant les cartes.

| Attribut / Méthode | Type | Description |
|--------------------|------|-------------|
| `paires` | `int` | Nombre de paires à trouver (`width × height // 2`) |
| `grid` | `list[list[Card]]` | Grille 2D contenant les objets `Card` |
| `binary_grid` | `list[list[int]]` | Grille 2D miroir : `0` = carte non trouvée, `1` = paire trouvée |
| `add_card()` | `None` | Pioche `paires` cartes uniques dans un deck, les duplique, mélange et remplit `grid` |
| `find_card(card)` | `None` | Marque à `1` dans `binary_grid` toutes les cases contenant la carte donnée |
| `full()` | `bool` | Retourne `True` si toutes les cases de `binary_grid` valent `1` |
| `draw()` | `None` | Affiche la grille dans le terminal (debug) |

> La grille accepte uniquement des dimensions dont le produit est pair. Une grille impaire affiche `"mauvaise taille"` et n'est pas initialisée.

---

## Fonctions d'affichage : `display.py`

| Fonction | Retour | Description |
|----------|--------|-------------|
| `main_menu()` | `bool` | Affiche le menu principal. `True` = nouvelle partie, `False` = quitter |
| `card_choice(grid, found_cards, choices, pause)` | `tuple \| bool \| None` | Gère l'interaction du joueur. En mode normal retourne `(card, cord)` au clic sur une carte valide. En mode `pause=True` retourne `True` au premier clic (n'importe où). Retourne `None` si fermeture |
| `display_cards(grid, grid_colid, found_cards, choices)` | `None` | Redessine toutes les cartes : face visible pour les paires trouvées et les choix en cours, dos pour les autres |
| `display_title()` | `None` | Affiche le titre *Memory* avec effet d'ombre |
| `display_main_menu(msg_new_game, msg_leave)` | `None` | Affiche les boutons du menu principal |

### Constantes globales

| Variable | Valeur | Description |
|----------|--------|-------------|
| `screen` | `Surface 700×700` | Fenêtre principale pygame |
| `card_back` | `Surface` | Image du dos de carte |
| `card_sprites` | `dict` | Dictionnaire `(valeur, couleur)` → image pygame |
| `tapis` | `Surface` | Image de fond du tapis de jeu |

### Coordonnées des cartes

Les positions sont calculées dynamiquement dans `card_choice()` :

```
x = 135 + colonne × 110
y = 30  + ligne   × 160
```

---

## Boucle principale : `memory.py`

### Schéma de la boucle

```
main_menu()
└── while run
    ├── Grid(4, 4) + add_card()          ← nouvelle grille de 16 cartes (8 paires)
    └── while play
        ├── card_choice()                ← 1er choix du joueur
        ├── card_choice()                ← 2e choix du joueur
        ├── card_choice(pause=True)      ← affichage des deux cartes, attente d'un clic
        ├── comparaison des deux choix
        │   └── si paire trouvée → find_card() + found_cards
        └── grid.full() → main_menu()   ← fin de partie
```

---

## Assets : `assets.py`

### `load_assets()`

Charge toutes les ressources graphiques depuis le dossier `Assets/` :

| Variable retournée | Type | Description |
|--------------------|------|-------------|
| `cartes_dos` | `Surface` | Image du dos de carte |
| `dico_de_cartes` | `dict` | Dictionnaire `(valeur, couleur)` → image pygame |
| `tapis` | `Surface` | Image de fond du tapis de jeu |

**Couleurs disponibles :**

| Code | Couleur |
|------|---------|
| `co` | ♥ Cœur |
| `p`  | ♠ Pique |
| `ca` | ♦ Carreau |
| `t`  | ♣ Trèfle |

> Taille des cartes : **100 × 150 px** · Taille de la fenêtre : **700 × 700 px**
