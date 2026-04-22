# create_db.py

import sqlite3
from pathlib import Path

# On définit où sera créée la base de données (dans un dossier appelé database).
DB_folder = Path(__file__).parent
DB_folder.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_folder / 'game.db'


def create_db():
    # Connexion à SQLite (si le fichier n'existe pas, il sera créé automatiquement)
    con = sqlite3.connect(DB_PATH)
    con.execute(
        "PRAGMA foreign_keys = ON")  # IMPORTANT! PRAGMA foreign_keys = ON, doit être exécutée à chaque nouvelle connexion.
    cur = con.cursor()
    print("Connexion réussie ✔️")

    # Création des tables (schéma DB)

    cur.executescript("""
        -- Créer la TABLE des créatures
        CREATE TABLE IF NOT EXISTS creatures (
            id_creature INTEGER PRIMARY KEY AUTOINCREMENT,
            name_creature TEXT UNIQUE,
            hp_initial INTEGER, 
            attack_value INTEGER,
            defense_value INTEGER,
            spec_attack_name TEXT,
            spec_attack_value INTEGER,
            spec_attack_descr TEXT
        );

        -- Créer la table des joueurs

        CREATE TABLE IF NOT EXISTS players (
            id_player INTEGER PRIMARY KEY AUTOINCREMENT,
            name_player TEXT,
            id_creature INTEGER,
            FOREIGN KEY (id_creature) REFERENCES creatures(id_creature)
        );

        -- Créer la table de l'historique de combats

        CREATE TABLE IF NOT EXISTS history (
            id_battle INTEGER PRIMARY KEY AUTOINCREMENT,
            id_player_winner INTEGER,
            id_creature INTEGER,
            date DATETIME,
            FOREIGN KEY (id_player_winner) REFERENCES players(id_player),
            FOREIGN KEY (id_creature) REFERENCES creatures(id_creature)
        );

        -- Créer la table du Code pin pour auth_user

        CREATE TABLE IF NOT EXISTS pin (
            id_pin INTEGER PRIMARY KEY AUTOINCREMENT,
            pin TEXT,
            id_user INTEGER,
            FOREIGN KEY (id_user) REFERENCES players(id_player)
        );

        """)

    # Liste des créatures jouables
    creatures = [
        #   (name_creature, hp_initial, attack_value, defense_value, spec_attack_name, spec_attack_value, spec_attack_descr)
        ("Démon", 50, 9, 5, "Épée de l'Enfer", 18, "Inflige de lourds dégâts bruts"),
        ("Troll", 65, 7, 7, "Rage", 12, "Double l'attaque pendant un tour"),
        ("Sorcière", 40, 8, 4, "Malédiction", 3, "Réduit l'attaque adverse de -3 pendant 2 tours"),
        ("Licorne", 45, 7, 8, "Soin magique", 12, "Restaure 12 PV, utilisable une fois"),
        ("Centaure", 55, 9, 6, "Charge rapide", 4, "Inflige un dégât doublé mais perd 4 PV en contre-coup"),
        ("Guerrier noir", 60, 8, 7, "Parade Héroïque", 0, "Bloque complètement la prochaine attaque"),
        ("Dragon", 55, 10, 6, "Souffle de feu", 20, "Brûle l'ennemi, perte de PV par tour"),
        ("Loup-garou", 50, 9, 6, "Appel de la meute", 4, "Inflige un dégât multiplié par 3"),
        ("Elfe", 45, 8, 5, "Tir précis", 10, "Inflige 10 dégâts garantis en ignorant la défense")
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO creatures (name_creature, hp_initial, attack_value, defense_value, spec_attack_name, spec_attack_value, spec_attack_descr)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, creatures)

    #  Liste des joueurs (test)
    #  name_player, id_creature (creature choisie)

    players = [
        ("admin", 3)
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO players (name_player, id_creature)
        VALUES (?, ?)
    """, players)

    # On valide les changements (commit) et on ferme la connexion
    print("Database créée avec succès ✔️.")
    con.commit()
    con.close()
    print("Déconnexion ✔️")

if __name__ == "__main__":
    create_db()

# Special_attacks :
# Catalogue des attaques spéciales.
# Exemple : "souffle_de_feu" est de type "damage" avec une valeur de 3.

# Creatures :
# Chaque créature a une attaque spéciale associée via spec_attack_name.
# Exemple : "Dragon" a spec_attack_name = "souffle_de_feu".

# History :
# Sert de journal pour voir les combats précedents.
# Exemple : après une partie, on insère "Joueur 1 vs Joueur 2, gagnant Joueur 1 avec x tours".