# Bataille

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

> Jeu de cartes **Bataille** en Python avec interface graphique pygame.
> Le joueur affronte l'ordinateur avec la possibilité de **choisir quelle carte jouer** parmi ses deux prochaines.

---

## Table des matières

- [Démarrer le programme](#démarrer-le-programme)
- [Comment jouer](#comment-jouer)
- [Structure du projet](#structure-du-projet)
- [Classes et méthodes](#classes-et-méthodes)
- [Fonctions d'affichage](#fonctions-daffichage--displaypy)
- [Boucle principale](#boucle-principale--bataillepy)
- [Assets](#assets--assetspy)

---

## Démarrer le programme

### Dépendances

**Bibliothèques standard** *(incluses avec Python, aucune installation nécessaire)* :

| Module | Utilisation |
|--------|-------------|
| `random` | Mélange des cartes et redistribution aléatoire des plis |

**Bibliothèques à installer** :

```bash
pip install pygame
```

| Module | Utilisation |
|--------|-------------|
| `pygame` | Affichage, gestion des événements clavier/souris et chargement des images |

### Lancement

```bash
python bataille.py
```

---

## Comment jouer

1. **Menu principal** - Cliquer sur *Nouvelle partie* pour lancer une partie, ou *Quitter* pour fermer.
2. **Choisir sa carte** - À chaque tour, vos deux prochaines cartes s'affichent en bas à gauche. Cliquez sur celle que vous voulez jouer. La carte de l'adversaire est visible à droite pour vous aider à choisir.
3. **Résultat du tour** - Les deux cartes jouées s'affichent au centre. Le joueur avec la carte la plus haute remporte le pli.
4. **Égalité (guerre)** - Si les deux cartes sont identiques, chaque joueur pose une carte supplémentaire et vous choisissez à nouveau votre carte pour la guerre.
5. **Fin de partie** - Le joueur qui remporte toutes les cartes gagne. Un écran de fin s'affiche avec le vainqueur.

> **As** = carte la plus forte (valeur 14)

---

## Structure du projet

```
├── bataille.py                        # Point d'entrée, boucle principale
└── Library/
    ├── Class/
    │   ├── Deck52.py                  # Classes Card et Deck
    │   ├── Player.py                  # Classe Player
    │   └── Trick.py                   # Classe Trick
    └── Jeux/Bataille/Front/
        ├── display.py                 # Fonctions d'affichage pygame
        └── assets.py                  # Chargement des ressources graphiques
```

---

## Classes et méthodes

### `Card` : `Deck52.py`

Représente une carte du jeu.

| Attribut / Méthode | Type | Description |
|--------------------|------|-------------|
| `card` | `tuple` | Tuple `(valeur, couleur)` ex: `("7", "t")` |
| `value` | `str` | Valeur string de la carte ex: `"7"` |
| `color` | `str` | Couleur de la carte ex: `"t"` |
| `values` | `dict` | Conversion string → int (`"1"` → 14, `"2"` → 2, ...) |

---

### `Deck` : `Deck52.py`

Représente un jeu de 52 cartes.

| Attribut / Méthode | Type | Description |
|--------------------|------|-------------|
| `deck` | `list[Card]` | Liste de toutes les cartes |
| `new_deck()` | `None` | Génère les 52 cartes (4 couleurs × 13 valeurs) |
| `draw(player, number)` | `None` | Distribue `number` cartes vers la main d'un joueur |
| `shuffle()` | `None` | Mélange le deck |

**Couleurs disponibles :**

| Code | Couleur |
|------|---------|
| `co` | ♥ Cœur |
| `p` | ♠ Pique |
| `t` | ♣ Trèfle |
| `ca` | ♦ Carreau |

---

### `Player` : `Player.py`

Représente un joueur (humain ou ordinateur).

| Attribut / Méthode | Type | Description |
|--------------------|------|-------------|
| `name` | `str` | Nom du joueur |
| `hand` | `list[Card]` | Main du joueur |
| `drop()` | `Card` | Retire et retourne la première carte de la main (`pop(0)`) |

---

### `Trick` : `Trick.py`

Représente le pli en cours (les cartes posées sur la table).

| Attribut / Méthode | Type | Description |
|--------------------|------|-------------|
| `cards` | `list[Card]` | Cartes posées dans l'ordre `p1, p2, p1, p2...` |
| `__str__()` | `str` | Affiche le pli sous la forme `7(t) \| 9(ca)` |
| `result(p1, p2)` | `bool` | Détermine le gagnant du pli |

**Logique de `result(p1, p2)`** :

| Situation | Résultat |
|-----------|----------|
| `p1 > p2` | p1 remporte toutes les cartes du pli (mélangées) → `False` |
| `p1 < p2` | p2 remporte toutes les cartes du pli (mélangées) → `False` |
| `p1 == p2` + assez de cartes | Guerre : chaque joueur pose une carte supplémentaire → `True` |
| `p1 == p2` + pas assez de cartes | Redistribution équitable → `False` |

---

## Fonctions d'affichage : `display.py`

| Fonction | Retour | Description |
|----------|--------|-------------|
| `main_menu()` | `bool` | Affiche le menu principal. `True` = nouvelle partie, `False` = quitter |
| `display_main_menu(new_game_msg, leave_msg, title, title_)` | `None` | Place les boutons du menu principal et le titre sur l'écran |
| `display_num_of_card(p1, p2)` | `None` | Affiche le nombre de cartes restantes pour chaque joueur |
| `display_table(trick, p1, p2)` | `list` | Affiche le plateau avec le tapis, les cartes en jeu et les mains |
| `display_choose(trick, p1, p2)` | `int` | Affiche les 2 prochaines cartes du joueur et attend un clic. `0` ou `1` selon le choix |
| `display_game_over(p1, p2)` | `bool` | Affiche l'écran de fin. `True` = rejouer, `False` = quitter |

---

## Boucle principale : `bataille.py`

### `player_turn()`

Gère un tour complet du joueur :

1. Affiche les 2 prochaines cartes via `display_choose()`
2. Swap la carte choisie en position `0`
3. Chaque joueur pose sa carte sur le pli
4. Affiche le résultat via `display_table()`
5. Retourne `True` si la partie continue

### Schéma de la boucle

```
main_menu()
└── while les deux joueurs ont des cartes
    ├── player_turn()                ← le joueur choisit sa carte
    └── while trick.result() == True (guerre)
        └── player_turn()            ← le joueur choisit sa carte pour la guerre
```

---

## Assets : `assets.py`

### `load_assets()`

Charge toutes les ressources graphiques depuis le dossier `Assets/` :

| Variable retournée | Description |
|--------------------|-------------|
| `deck_png` | Liste de tuples `((valeur, couleur), image)` |
| `carte_dos` | Image du dos de carte |
| `cards_sprite` | Dictionnaire `(valeur, couleur)` → image pygame |
| `tapis` | Image de fond du tapis de jeu |

> Taille des cartes : **100 × 150 px** - Taille de la fenêtre : **700 × 700 px**
