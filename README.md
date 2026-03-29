Bienvenue dans ma collection de jeux de cartes ! Ce `README.md` explique les rêgles des différents jeux, leurs fonctionnement et comment lancer les jeux.

---

**Contenu**

* I. **Liste des jeux disponibles.**
* II. **Règles.**
* III. **Fonctionnement.**
* IV. **Explication du code**
* V. **Instalation et démarage**
* VI. **Crédits**

---

**I. Liste des jeux disponibles.**

  1. **Bataille.**
  
    - Nombre de joueurs : 1 + Ordinateur
    
    - Matériel : Un jeu de 52 cartes
    
    - Objectif : Gagner toutes les cartes du jeu


  2. **Memory.**
    
    - Nombre de joueurs : 1
    
    - Matériel : Cartes disposées en grille (paires)
    
    - Objectif : Retrouver toutes les paires de cartes


  3. **Uno.**

    - Nombre de joueurs : 1 joueur + 3 Ordinateur
  
    - Matériel : Jeu de cartes UNO
  
    - Objectif : Être le premier à ne plus avoir de cartes

---
    
**II. Règles.**

  1. **Bataille.**
  
  * **Règles principales** :

    * Le paquet est mélangé puis distribué équitablement entre les deux joueurs.
    * Chaque joueur joue une carte en même temps.
    * Le joueur avec la carte la plus forte remporte le pli.
    * En cas d’égalité, une « bataille » est déclenchée avec plusieurs cartes en jeu.
    * Le jeu continue jusqu’à ce qu’un joueur récupère toutes les cartes.
      


  2. **Memory.**
     
  * **Règles principales** :
  
    * Les cartes sont mélangées et placées face cachée dans une grille
    * Le joueur retourne deux cartes à chaque tour
    * Si les cartes sont identiques, elles restent visibles
    * Sinon, elles sont retournées face cachée
    * Le jeu se termine lorsque toutes les paires sont trouvées


  3. **Uno.**
     
  * **Règles principales** :

    * Les joueurs jouent chacun leur tour une carte compatible (même couleur ou valeur)
    * Certaines cartes ont des effets : +2, +4, inversion, passe
    * Si un joueur ne peut pas jouer, il pioche
    * Le premier joueur sans cartes gagne

---

**III. Fonctionnement**

  1. **Bataille.** 
  
  - Utilisation de classes comme `Deck`, `Player` et `Pli` pour gérer la logique du jeu.
  - Mélange aléatoire du deck avec `random.shuffle`.
  - Interface graphique réalisée avec la bibliothèque `pygame`.
  - Menu principal interactif avec options "Nouvelle partie" et "Quitter".
  - Affichage des cartes, du tapis et du nombre de cartes restantes en temps réel.
    

  2. **Memory.**
  
  - `memory.py` gère la boucle principale du jeu (sélection de cartes et vérification des paires)
  - Une grille (classe `Grid`) contient les cartes et suit celles déjà trouvées
  - `add_card()` crée des paires de cartes aléatoires et les mélange
  - `display.py` gère l’affichage avec pygame (grille, cartes visibles/cachées, clics souris)
  - `choix_cartes()` permet au joueur de cliquer sur une carte
  - Le jeu s’arrête quand toutes les cartes sont trouvées (`full()`)


  3. **Uno.**

  - `uno.py` gère toute la logique principale (tour par tour, joueur humain + IA)
  - `DeckUno.py` crée les cartes UNO et mélange le deck
  - `Engine.py` contient les règles du jeu (cartes jouables, effets, distribution)
  - `display.py` gère l’affichage avec pygame (cartes, main du joueur, clics)
  - Les autres joueurs sont contrôlés automatiquement (IA simple)

---

**IV. Explication du code**

  1. **Bataille** :
     
  Le jeu est organisé en plusieurs fichiers qui travaillent ensemble.
  
  * **bataille.py** :
  
    * C’est le fichier principal qui lance le jeu
    * Il crée un deck de 52 cartes, le mélange, puis distribue 26 cartes à chaque joueur
    * Il gère la boucle principale du jeu (tant que les joueurs ont des cartes)
    * À chaque tour, les joueurs posent une carte et le programme détermine le gagnant du pli
  
  * **assets.py** :
  
    * Charge toutes les images (cartes, tapis, dos de carte)
    * Redimensionne les images pour l’affichage
    * Prépare un dictionnaire pour associer chaque carte à son image
  
  * **display.py** :
  
    * Gère toute l’interface graphique avec pygame
    * Affiche le menu principal (nouvelle partie / quitter)
    * Affiche le jeu en cours (cartes jouées, nombre de cartes restantes)
    * Met à jour l’écran à chaque tour

    En résumé :
    
    * `bataille.py` = logique du jeu
    * `assets.py` = ressources graphiques
    * `display.py` = affichage et interactions


  2. **Memory** :
     
  Le jeu Memory fonctionne de manière similaire à Bataille.
  
  * **memory.py** :
  
    * Initialise une grille 4x4 (donc 8 paires)
    * Lance le menu puis la boucle de jeu
    * Gère les choix du joueur (2 cartes)
    * Vérifie si les cartes sont identiques
    * Met à jour la liste des cartes trouvées
  
  * **Grid.py** :
  
    * Crée la grille de jeu
    * Place les cartes en paires aléatoires
    * Garde une trace des cartes déjà trouvées avec une grille binaire
    * Permet de vérifier si le jeu est terminé
  
  * **display.py** :
  
    * Affiche la grille avec pygame
    * Gère les clics du joueur
    * Montre les cartes retournées temporairement
  
    En résumé :
    
    * `memory.py` = logique du jeu
    * `Grid.py` = structure et données
    * `display.py` = interface graphique

  3. **Uno** :

  Explication rapide du code (UNO)
  
  * **uno.py** :
  
    * Initialise la partie (deck, joueurs, première carte)
    * Gère la boucle principale du jeu
    * Différencie le joueur réel (clic souris) et les bots
    * Applique les règles spéciales (Draw, joker, inversion…)
  
  * **DeckUno.py** :
  
    * Crée toutes les cartes UNO (couleurs + valeurs)
    * Mélange le deck
    * Permet de piocher et trier les cartes
  
  * **Engine.py** :
  
    * Contient toute la logique du jeu :
  
      * vérifier si une carte est jouable
      * appliquer les effets (+2, +4, skip…)
      * gérer les tours et la direction
  
  * **display.py** :
  
    * Affiche le jeu (cartes du joueur, dos des adversaires)
    * Gère les clics pour jouer une carte
    * Permet de choisir une couleur pour les jokers
    * Affiche la fin de partie
  
    En résumé :
    
    * `uno.py` = moteur principal
    * `Engine.py` = règles du jeu
    * `DeckUno.py` = cartes et deck
    * `display.py` = interface graphique

---

**V. Installation et démarage**
  
  1. **Matériel nécessaire.**
  
  * Un ordinateur (Windows, Mac ou Linux)
  * Une souris (pour interagir avec les jeux)

Pour faire fonctionner les jeux sur ton ordinateur :

  2. Installer Python
  
  * Télécharge Python depuis le site officiel : [https://www.python.org](https://www.python.org)
  * Pendant l’installation, coche **"Add Python to PATH"**
  * Vérifie l’installation avec :
  
    ```bash
    python --version
    ```

  3. Installer pygame
  
  * Ouvre un terminal (cmd, PowerShell ou terminal Linux/Mac)
  * Installe pygame avec :
  
    ```bash
    pip install pygame
    ```

  4. Télécharger le projet
  
  * Clone ou télécharge ton projet
  
    ```bash
    git clone <ton-repo>
    ```
  * Ou décompresse l’archive si tu l’as en .zip

  5. Lancer un jeu
  
  * Place-toi dans le dossier du jeu
  * Lance le fichier principal :
  
    ```bash
    python "NomDuJeu".py
    ```

---

Comment utiliser

1. Choisir un jeu
2. Lire les règles
3. Préparer le matériel
4. Jouer et s'amuser !

---

**VI. Crédits**

**FRINGANT Aubin** 
BTS SIO 
