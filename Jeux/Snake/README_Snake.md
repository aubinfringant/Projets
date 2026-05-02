# Snake

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green?logo=pygame&logoColor=white)

> Jeu de **Snake** en Python avec interface graphique pygame.
> Mangez des pommes pour grandir et évitez de vous cogner contre les murs ou votre propre queue.

---

## Table des matières

- [Démarrer le programme](#démarrer-le-programme)
- [Comment jouer](#comment-jouer)
- [Structure du projet](#structure-du-projet)
- [Classe Snake](#classe-snake--snakepy)
- [Classe Apple](#classe-apple--applepy)
- [Fonctions d'affichage](#fonctions-daffichage--displaypy)
- [Boucle principale](#boucle-principale--snakepy)
- [Assets](#assets--assetspy)

---

## Démarrer le programme

### Lancement

```
snake.py
```

---

## Comment jouer

1. **Menu principal** - Cliquer sur *Nouvelle partie* pour lancer une partie, ou *Quitter* pour fermer.
2. **Préparation** - Appuyer sur n'importe quelle touche ou cliquer pour démarrer le jeu.
3. **Diriger le serpent** - Utiliser les **flèches du clavier** pour se diriger (haut, bas, gauche, droite).
4. **Manger les pommes** - Chaque pomme mangée agrandit le serpent et augmente le score.
5. **Éviter les obstacles** - Ne pas toucher les murs ni la propre queue du serpent.
6. **Victoire** - Manger 140 pommes remplit la grille complètement et vous gagnez.
7. **Défaite** - Toucher un mur ou la propre queue = fin de partie. Appuyer sur **Espace** pour recommencer.

> **Score objectif** : 140 pommes - **Vitesse** : 4 FPS

---

## Structure du projet

```
└── Projets/
    ├── Class/
    │   ├── Snake.py                       # Classe Snake
    │   └── Apple.py                       # Classe Apple
    └── Jeux/Snake/
             ├── Front/
             │   ├── display.py                     # Fonctions d'affichage pygame
             │   └── assets.py                      # Chargement des ressources graphiques
             └── snake.py                               # Point d'entrée, boucle principale
```

---

## Classe Snake : `Snake.py`

Représente le serpent du joueur.

| Attribut                      | Type                | Description                                                           |
|-------------------------------|---------------------|-----------------------------------------------------------------------|
| `grow`                        | `bool`              | `True` si le serpent doit grandir au prochain mouvement               |
| `direction`                   | `list[tuple]`       | Queue de direction : `[direction_actuelle, direction_avant_dernière]` |
| `old_direction`               | `tuple`             | Direction précédente du serpent                                       |
| `grid_cord`                   | `list[list[tuple]]` | Grille 12×12 des coordonnées en pixels                                |
| `grid_index`                  | `list[tuple]`       | Grille 12×12 des indices (i, j)                                       |
| `snake`                       | `list[list]`        | Liste des segments : `[[image, (ligne, colonne)], ...]`               |
| `heads`, `bodys`, `tails`     | `list`              | Images des têtes, corps et queues dans 4 orientations                 |
| `turn_horaires`, `turn_antis` | `list`              | Images des virages horaires et anti-horaires                          |

| Méthode               | Retour    | Description                                                       |
|-----------------------|-----------|-------------------------------------------------------------------|
| `get_cord(segment)`   | `tuple`   | Retourne les coordonnées en pixels du segment                     |
| `get_grid_cord(i, j)` | `tuple`   | Retourne les coordonnées en pixels pour l'indice (i, j)           |
| `turn(direction)`     | `None`    | Ajoute une direction à la queue (limite à 2 directions maximum)   |
| `get_img_idx()`       | `int`     | Retourne l'index d'image correspondant à la direction actuelle    |
| `get_body_img()`      | `Surface` | Retourne l'image du corps au virage                               |
| `get_tail_img_idx()`  | `int`     | Retourne l'index d'image de la queue                              |
| `move()`              | `bool`    | Bouge le serpent d'une case. Retourne `False` en cas de collision |

---

## Classe Apple : `Apple.py`

Représente les pommes à manger.

| Attribut   | Type          | Description                                                                                       |
|------------|---------------|---------------------------------------------------------------------------------------------------|
| `position` | `list[tuple]` | Liste des positions des pommes actuellement actives `(ligne, colonne)`                            |
| `eaten`    | `int`         | Nombre total de pommes mangées                                                                    |

| Méthode                     | Retour  | Description                                                                                       |
|-----------------------------|---------|---------------------------------------------------------------------------------------------------|
| `random_position(snake)`    | `tuple` | Génère une position aléatoire valide (pas sur le serpent, pas hors limites). Retourne la position |
| `add_to_bag(position)`      | `None`  | Ajoute une position à la liste des pommes                                                         |
| `remove_from_bag(position)` | `None`  | Retire une position de la liste et incrémente le compteur                                         |

---

## Fonctions d'affichage : `display.py`

| Fonction                         | Retour  | Description                                                                                  |
|----------------------------------|---------|----------------------------------------------------------------------------------------------|
| `intro(snake, apple)`            | `None`  | Petite pause avant de commencer (pour se préparer mentalement). Attend un clic ou une touche |
| `display_all(snake, apple)`      | `None`  | Gère l'affichage de la partie (serpent, pommes, grille)                                      |
| `display_game_over(apple_eaten)` | `bool`  | Gère l'affichage de la fin de la partie. `True` = rejouer, `False` = quitter                 |
| `fondu()`                        | `None`  | Petite animation de fondu d'ouverture                                                        |

---

## Boucle principale : `snake.py`

### Schéma de la boucle

```
fondu()
└── while main_menu()
    └── while True
        ├── Snake() + Apple()            ← création du serpent et des pommes
        ├── intro()                      ← pause avant démarrage
        ├── while len(apple.position) < 4  ← remplissage initial des pommes
        └── while True
            ├── for event (clics clavier)  ← direction du serpent
            ├── snake.move()               ← mouvement et détection collision
            ├── comparaison position tête vs pommes
            │   └── si mangée → snake.grow = True + remove_from_bag()
            ├── if len(pommes) < 4 → ajouter pomme aléatoire
            └── display_all()            ← affichage du jeu
                └── clock.tick(4)        ← 4 FPS (1 mouvement par 250ms)
```

---

## Assets : `assets.py`

### `load_assets()`

Charge toutes les ressources graphiques depuis le dossier `Assets/` :

| Variable retournée  | Description                                                 |
|---------------------|-------------------------------------------------------------|
| `apple`             | Image de la pomme (45×45 px)                                |
| `grid`              | Image de la grille de jeu (540×540 px)                      |
| `head`              | Liste 4 images de la tête (4 orientations)                  |
| `body`              | Liste 4 sous-listes × 15 images du corps avec animations    |
| `tail`              | Liste 4 sous-listes × 15 images de la queue avec animations |
| `turn_horaire`      | Liste 4 images des virages horaires                         |
| `turn_anti`         | Liste 4 images des virages anti-horaires                    |

---

## Mécanique de jeu

### Croissance du serpent

Le serpent commence avec 4 segments : tête + 2 corps + queue.
À chaque `move()` :
1. Crée un nouveau segment tête à la position suivante
2. Si `grow = False`, retire le dernier segment (la queue)
3. Si `grow = True`, garde le dernier segment (agrandissement) et réinitialise `grow`

### Détection de collision

`move()` retourne `False` si :
- Nouvelle tête en dehors de `(0,0) à (11,11)` (murs)
- Nouvelle tête sur un autre segment (hors queue si grow = False) du serpent  (auto-collision)

### Système de pommes

Maximum de 4 pommes à l'écran simultanément.
À chaque fois qu'une pomme est mangée :
1. `grow = True` (agrandissement lors du prochain mouvement)
2. Appel à `apple.remove_from_bag()` (compteur +1)
3. Si `len(apple.position) < 4`, une nouvelle pomme est générée aléatoirement
