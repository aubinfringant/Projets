# Memory

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

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

## Démarrer le programme

### Dépendances

**Bibliothèques standard** *(incluses avec Python, aucune installation nécessaire)* :

| Module | Utilisation |
|--------|-------------|
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

1. **Menu principal** - Cliquer sur *Nouvelle partie* pour lancer une partie, ou *Quitter* pour fermer.
2. **Retourner une carte** - Cliquer sur une carte face cachée pour la révéler.
3. **Retourner une seconde carte** - Cliquer sur une autre carte. Si les deux cartes sont identiques, elles restent visibles.
4. **Continuer** - Si les deux cartes sont différentes, cliquer n'importe où pour les retourner face cachée et passer au tour suivant.
5. **Fin de partie** - Lorsque toutes les paires sont trouvées, le menu principal s'affiche pour rejouer.

---

## Structure du projet

```
├── memory.py                              # Point d'entrée, boucle principale
└── Library/
    ├── Class/
    │   ├── Deck52.py                      # Classes Card et Deck
    │   └── GridMemory.py                  # Classe Grid
    └── Jeux/Memory/Front/
        ├── display.py                     # Fonctions d'affichage pygame
        └── assets.py                      # Chargement des ressources graphiques
```

---

## Classe Grid : `GridMemory.py`

Représente la grille de jeu contenant les cartes.

| Attribut / Méthode | Type | Description |
|--------------------|------|-------------|
| `paires` | `int` | Nombre de paires à trouver (`width × height // 2`) |
| `grid` | `list[list[Card]]` | Grille 2D contenant les objets `Card` |
| `binary_grid` | `list[list[int]]` | Grille 2D miroir : `0` = carte non trouvée, `1` = paire trouvée |
| `add_card()` | `None` | Pioche `paires` cartes uniques, les duplique, mélange et remplit `grid` |
| `find_card(card)` | `None` | Marque à `1` dans `binary_grid` toutes les cases contenant la carte donnée |
| `full()` | `bool` | Retourne `True` si toutes les cases de `binary_grid` valent `1` |
| `print_r()` | `None` | Affiche la grille dans le terminal (debug) |

---

## Fonctions d'affichage : `display.py`

| Fonction | Retour | Description |
|----------|--------|-------------|
| `main_menu()` | `bool` | Affiche le menu principal. `True` = nouvelle partie, `False` = quitter |
| `display_title(title, title_)` | `None` | Affiche le titre *Memory* avec effet d'ombre |
| `display_main_menu(msg_new_game, msg_leave)` | `None` | Affiche les boutons du menu principal |
| `card_choice(grid, found_cards, choices)` | `tuple` | Gère la sélection d'une carte. Retourne `(card, cord)` au clic sur une carte valide. Retourne `None` si fermeture |
| `display_cards(grid, grid_colid, found_cards, choices)` | `None` | Redessine toutes les cartes : face visible pour les paires trouvées et les choix en cours, dos pour les autres |
| `confirmation(grid, found_cards, choices)` | `None` | Fais une pause pour bien mémoriser les deux cartes différentes |

---

## Boucle principale : `memory.py`

### Schéma de la boucle

```
main_menu()
└── while run
    ├── Grid(4, 4) + add_card()          ← nouvelle grille de 16 cartes (8 paires)
    └── while len(found_cards) != 8
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

> Taille des cartes : **100 × 150 px** - Taille de la fenêtre : **700 × 700 px**
