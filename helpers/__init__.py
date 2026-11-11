import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv("DATABASE")#"censoescolar.db" posso colocar de valor padrão dps, mas fica paia


def get_db_connection():
    conn = None

    try:
        conn = sqlite3.connect(DATABASE)
        print("Conectou!")

    except sqlite3.Error as e:
        print(f"Erro ao conectar no DATABASE: {e}")

    return conn