import sqlite3

connection = None

try:
    connection = sqlite3.connect('./censoescolar.db')
    
    with open('./db/schema.sql') as file:
        connection.executescript(file.read())
        
except sqlite3.Error as e:
    print(f"SQLite throws a Exception: {e}")

finally:
    if connection is not None:    
        connection.close()



  


