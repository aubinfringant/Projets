Bienvenue dans ma collection de jeux (Cartes, Minis Jeux)! Ce `README.md` resume les rêgles des différents jeux et comment les lancer.

---

**Contenu**

**I. Liste des jeux disponibles.  
II. Instalation et démarage.
III. Class commune
IV. Crédits.**

---

**I. Liste des jeux disponibles.**

  1. **Bataille.**
  
    - Nombre de joueurs : 1 + Ordinateur
    
    - Objectif : Gagner toutes les cartes du jeu


  2. **Memory.**
    
    - Nombre de joueurs : 1
    
    - Objectif : Retrouver toutes les paires de cartes


  3. **Puissance 4.**

    - Nombre de joueurs : 1 ou 2 joueurs
  
    - Objectif : Connecter 4 jetons de sa couleur avant l'adversaire

    
  4. **Snake.**

    - Nombre de joueurs : 1 joueur
  
    - Objectif : Manger le plus de pomme sans rentrer dans les murs ou se mordre la queue

    
  5. **Uno.**

    - Nombre de joueurs : 1 joueur + 3 Ordinateur
  
    - Objectif : Être le premier à ne plus avoir de cartes


---

**II. Installation et démarage**
  
1. **Matériel nécessaire**
  * Un ordinateur à jour
  * Une souris ou la pavé tactile (pour interagir avec les jeux)

2. **Installer Python et Pycharm**

  * Python : Télécharge-le sur python.org. Lors de l'installation, coche bien "Add Python to PATH". 
  * PyCharm : Télécharge et installe PyCharm Community Edition (gratuit) sur le site de JetBrains.

3. **Récupérer la liste de jeu**

  * Ouvre PyCharm. Sur l'écran d'accueil, clique sur le bouton "Get from VCS".
  * Dans le champ URL, colle le lien de ce dépôt :
```bash
  https://github.com/aubinfringant/Projets
  ```
  * Choisis le dossier où tu veux enregistrer le projet sur ton PC et clique sur "Clone".


4. **installer Pygame**

  * Ouvre l'onglet Terminal en bas de PyCharm.
  * Tape la commande suivante et appuie sur Entrée :

  ```bash 
  pip install pygame
  ```

5. **Lancer un jeu**

  * Dans l'explorateur de fichiers à gauche (onglet Project), fais un clic gauche sur le fichier du jeu que tu veux lancer (ex: Pussiance4 -> puissance4.py).

  * Sélectionne en haut le bouton lecture "Run 'NomDuJeu'".

---

Comment Jouer

1. Choisir un jeu
2. Lire le readme associé
3. Comprendre les rêgles
4. Jouer et s'amuser !

---

**III. Class commune**

### `GameStart.py`

Affiche le menu principale.

| Attribut         | Type      | Description                       |
|------------------|-----------|-----------------------------------|
| `title`          | `str`     | Titre du jeu                      |
| `color`          | `tuple`   | Couleur du fond                   |
| `width`,`height` | `int`     | Largeur et hauteur de l'écran     |
| `screen`         | `Surface` | Espace d'affichage (width,height) |

| Méthode               | Retour | Description                                           |
|-----------------------|--------|-------------------------------------------------------|
| `main_menu()`         | `bool` | Retourne `True` si click sur new_game ou stop le code |
| `display_main_menu()` | `None` | Place les boutons et titre sur l'écran                |


**IV. Crédits**

**FRINGANT Aubin** 
BTS SIO SLAM 1er année
