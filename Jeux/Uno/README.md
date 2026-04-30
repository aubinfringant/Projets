# UNO

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

> Jeu de **UNO** en Python avec interface graphique pygame.  
> Le joueur affronte trois bots en local dans une partie à 4 joueurs.

---

## Table des matières

- [Démarrer le programme](#-démarrer-le-programme)
- [Comment jouer](#-comment-jouer)
- [Structure du projet](#-structure-du-projet)
- [Fonctions moteur](#-fonctions-moteur--enginepy)
- [Fonctions d'affichage](#-fonctions-daffichage--displaypy)
- [Boucle principale](#-boucle-principale--unopy)
- [Assets](#-assets--assetspy)

---

## Démarrer le programme

### Dépendances

**Bibliothèques standard** *(incluses avec Python, aucune installation nécessaire)* :

| Module | Utilisation |
|--------|-------------|
| `os` | Construction des chemins vers les assets graphiques |
| `random` | Choix de couleur aléatoire pour les jokers des bots |

**Bibliothèques à installer** :

```bash
pip install pygame
```

| Module | Utilisation |
|--------|-------------|
| `pygame` | Affichage, gestion des événements clavier/souris et chargement des images |

### Lancement

```bash
python uno.py
```

---

## Comment jouer

1. **Menu principal** — Cliquer sur *Nouvelle partie* pour lancer une partie, ou *Quitter* pour fermer.
2. **Jouer une carte** — Cliquer sur une carte de sa main (affichée en bas) pour la jouer. Seules les cartes compatibles avec la carte du dessus sont acceptées.
3. **Piocher** — Cliquer sur la pioche (à droite de la carte du dessus) si aucune carte jouable n'est disponible.
4. **Joker / Joker+4** — Si une de ces cartes est jouée, une interface de choix de couleur s'affiche.
5. **Cartes spéciales** — Les effets s'appliquent automatiquement après chaque carte jouée.
6. **Fin de partie** — Le premier joueur à vider sa main remporte la partie. Cliquer pour rejouer.

> **Joueur 1** = vous (bas de l'écran) · **Joueurs 2, 3, 4** = bots (gauche, haut, droite)

---

## Structure du projet

```
├── uno.py                                 # Point d'entrée, boucle principale
└── Library/
    ├── Class/
    │   └── DeckUno.py                     # Classe DeckUno
    └── Jeux/Uno/
        ├── Back/
        │   └── engine.py                  # Logique de jeu et gestion des tours
        └── Front/
            ├── display.py                 # Fonctions d'affichage pygame
            └── assets.py                  # Chargement des ressources graphiques
```

---

## Fonctions moteur : `engine.py`

### Fonctions principales

| Fonction | Retour | Description |
|----------|--------|-------------|
| `playing(deck, players, top, direction, counter, players_turn)` | `bool` | Boucle de jeu principale. Alterne les tours joueur/bot jusqu'à victoire ou fermeture. Retourne `True` pour rejouer, `False` pour quitter |
| `player_turn(deck, players, hand, next_hand, direction, players_turn, counter, top)` | `tuple` | Gère un tour du joueur humain : choix de carte, pioche, joker, effets. Retourne `(False×8)` si fermeture |
| `bot_turn(deck, players, hand, next_hand, direction, players_turn, counter, top)` | `tuple` | Gère un tour d'un bot : joue la première carte compatible ou pioche. Retourne `(False×8)` si fermeture |
| `distribute(nbplayers, nbcards, deck)` | `list[list[Card]]` | Distribue `nbcards` cartes à `nbplayers` joueurs depuis le deck |
| `choose_first_card(deck)` | `(Card, Deck)` | Pioche la première carte visible en évitant les jokers et les cartes Draw |

### Fonctions utilitaires

| Fonction | Retour | Description |
|----------|--------|-------------|
| `playable(card, top)` | `bool` | Vérifie si une carte est jouable sur la carte du dessus (même couleur, même valeur, ou joker) |
| `can_draw(hand, top)` | `bool` | Retourne `True` si aucune carte de la main n'est jouable (autorisation de piocher) |
| `get_top(hand, choice, deck)` | `Card` | Retire la carte choisie de la main, l'insère en tête de deck et la retourne comme nouvelle carte du dessus |
| `card_effects(top, direction, players_turn, counter, next_hand, deck)` | `tuple` | Applique les effets de la carte jouée (inversion, passage, +2, +4) |
| `have_draw(hand, card, top, deck, counter)` | `tuple` | Gère le cas où un joueur répond à un +2 avec un autre +2 (empilement du compteur) |
| `joker_reset(deck)` | `Deck` | Réinitialise la couleur de tous les jokers présents dans le deck à `None` |

### Effets des cartes spéciales

| Valeur | Effet |
|--------|-------|
| `"Turn"` | Inverse le sens du jeu (`direction × -1`) |
| `"Pass"` | Le joueur suivant passe son tour |
| `"Draw"` | Le joueur suivant pioche 2 cartes (empilable) |
| `"joker"` | Le joueur choisit la nouvelle couleur active |
| `"joker4"` | Le joueur suivant pioche 4 cartes et le joueur choisit la couleur |

---

## Fonctions d'affichage : `display.py`

| Fonction | Retour | Description |
|----------|--------|-------------|
| `main_menu()` | `bool` | Affiche le menu principal. `True` = nouvelle partie, `False` = quitter |
| `display(players, deck, top, sens)` | `(bool, list)` | Redessine l'état complet du jeu. Retourne `(True, grid)` où `grid` contient les coordonnées des cartes du joueur, ou `(False, None)` si fermeture |
| `card_choice(players, deck, top, sens)` | `(bool, int \| str \| None)` | Attend le clic du joueur. Retourne `(True, index)` pour une carte, `(True, "Draw")` pour la pioche, `(False, None)` si fermeture |
| `color_choice(card)` | `(bool, str \| None)` | Affiche les 4 couleurs disponibles après un joker. Retourne `(True, couleur)` ou `(False, None)` si fermeture |
| `game_over(winner)` | `bool` | Affiche l'écran de fin avec le numéro du gagnant. `True` = rejouer, `False` = quitter |
| `affichage_main_menu(title_, title, new_game, leave)` | `None` | Affiche les éléments du menu principal |

### Disposition de l'écran

| Zone | Position | Description |
|------|----------|-------------|
| Joueur 1 (vous) | Bas — `y = 525` | Cartes face visible, espacées dynamiquement |
| Joueur 2 (bot) | Gauche — `x = -90` | Cartes dos, pivotées à 90° |
| Joueur 3 (bot) | Haut — `y = 5` | Cartes dos, pivotées à 180° |
| Joueur 4 (bot) | Droite — `x = 630` | Cartes dos, pivotées à 270° |
| Carte du dessus | Centre — `(250, 275)` | Carte active visible |
| Pioche | Centre — `(350, 275)` | Dos de carte cliquable |

### Constantes globales

| Variable | Description |
|----------|-------------|
| `screen` | Fenêtre principale pygame 700×700 |
| `card_back` | Image du dos de carte |
| `dict_cards` | Dictionnaire `(valeur, couleur)` → image pygame |
| `carpet` | Image de fond du tapis |
| `joker` | Liste `[joker, joker4, fleche]` — images des cartes spéciales et de la flèche de direction |

---

## Boucle principale : `uno.py`

### Schéma de la boucle

```
main_menu()
└── while launch
    ├── DeckUno() + distribute()          ← création du deck et distribution (7 cartes × 4 joueurs)
    ├── choose_first_card()               ← tirage de la première carte visible
    └── playing()                         ← boucle de jeu
        └── while True
            ├── joker_reset()
            ├── player_turn()             ← tour du joueur humain
            │   ├── card_choice()         ← clic sur une carte ou la pioche
            │   ├── color_choice()        ← si joker joué
            │   └── card_effects()        ← application des effets
            └── bot_turn() × 3            ← tours des trois bots
                └── card_effects()        ← application des effets
                    └── game_over()       ← si un joueur a vidé sa main
```

---

## Assets : `assets.py`

### `load_assets()`

Charge toutes les ressources graphiques depuis le dossier `Assets/` :

| Variable retournée | Type | Description |
|--------------------|------|-------------|
| `card_back` | `Surface` | Image du dos de carte |
| `card_dict` | `dict` | Dictionnaire `(valeur, couleur)` → image pygame |
| `carpet` | `Surface` | Image de fond du tapis de jeu |
| `joker` | `list` | Liste `[joker, joker4, fleche]` — images des cartes spéciales et de la flèche |

**Couleurs disponibles :**

| Code | Couleur |
|------|---------|
| `v` | 🟢 Vert |
| `b` | 🔵 Bleu |
| `r` | 🔴 Rouge |
| `j` | 🟡 Jaune |

**Valeurs disponibles :**

| Type | Valeurs |
|------|---------|
| Chiffres | `0` à `9` |
| Spéciales | `"Turn"`, `"Pass"`, `"Draw"`, `"joker"`, `"joker4"` |

> Taille des cartes : **100 × 150 px** · Taille de la fenêtre : **700 × 700 px**
