# db_connect.py
import sqlite3
from pathlib import Path

# On importe uniquement depuis le bon module
from database.create_db import create_db, DB_PATH

# Si la DB n'existe pas, on la crée automatiquement
if not DB_PATH.exists():
    print("⚠️ Base de données absente, création automatique...")
    create_db()

def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        print("DB connectée ✔️")
        return conn, cursor
    except sqlite3.Error as error:
        print("Erreur de connexion à la base :", error)
        return None, None

def init_global_connection():
    global sqliteConnection, c
    sqliteConnection, c = get_connection()
    return sqliteConnection, c

# Initialisation par défaut
sqliteConnection, c = init_global_connection()

if __name__ == '__main__':
    get_connection()