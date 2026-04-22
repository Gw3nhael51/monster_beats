#  Monster Beats : Jeu de Combat CLI Tour par Tour

## Objectif du projet
Créer un **jeu de combat tour par tour** en ligne de commande où chaque joueur incarne une créature possédant ses propres statistiques, attaques et capacités spéciales.

Le projet utilise :
- **Python 3.11+**
- **SQLite** pour la gestion des utilisateurs, créatures et historique
- Une architecture modulaire pour séparer logique, base de données et interface CLI

Projet réalisé dans le cadre du module **INFDIPC1**.  

🔗 [https://github.com/Gw3nhael51/monster_beats](https://github.com/Gw3nhael51/monster_beats)

---

## 📁 Structure du dépôt

| Fichier / Dossier | Rôle |
|-------------------|------|
| `main.py` | Point d’entrée du programme |
| `menu.py` | Interface utilisateur (CLI) |
| `auth.py` | Authentification & gestion des utilisateurs |
| `game.py` | Logique du jeu |
| `battle.py` | Mécanique des combats |
| `history.py` | Gestion de l’historique |
| `database/` | Scripts de création & connexion SQLite |
| `todo.md` | Suivi des tâches |

---

# 🚀 Installation (Windows / Linux / macOS)

## 1 Prérequis
- **Python 3.11 ou supérieur**
- Git (optionnel mais recommandé)

Vérifier votre version Python :

```
python --version
```

ou

```
python3 --version
```

---

## 2 Cloner le projet

```
git clone https://github.com/Gw3nhael51/projet_cube_un
cd projet_cube_un
```

---

## 3 Créer un environnement virtuel

### 🪟 Windows
```
python -m venv .env
.env\Scripts\activate
```

### 🐧 Linux
```
python3 -m venv .env
source .env/bin/activate
```

### 🍎 macOS
```
python3 -m venv .env
source .env/bin/activate
```

---

## 4 Installer les dépendances

```
pip install -r requirements.txt
```

---

## 5 Initialiser la base de données

La base se crée automatiquement au lancement, mais vous pouvez la générer manuellement :

```
python database/create_db.py
```

---

## 6 Lancer le jeu

```
python main.py
```

ou selon votre OS :

```
python3 main.py
```

---

# 🧪 Tests unitaires (optionnel)

```
pytest
```

---

# 📌 Notes importantes
- La base SQLite se trouve dans le dossier `database/`.
- Si vous rencontrez une erreur du type *"no such table: players"*, supprimez `game.db` et relancez `create_db.py`.
- Le jeu fonctionne entièrement en ligne de commande.

---

## 👥 Équipe projet
- [Gw3nhael51](https://github.com/Gw3nhael51)  
- [natalka-dev](https://github.com/natalka-dev)  
- [NileABDI](https://github.com/NileABDI)