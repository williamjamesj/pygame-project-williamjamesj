import sqlite3
cursy = sqlite3.connect("save.data").cursor()
cursy.execute("""CREATE TABLE IF NOT EXISTS saves (
                    id integer PRIMARY KEY,
                    coins integer NOT NULL,
                    level_complete integer NOT NULL,
                    owned_ships TEXT NOT NULL
                );
""")
cursy.close()
def load():
    cursy = sqlite3.connect("save.data").cursor()
    data = cursy.execute("""SELECT coins,level_complete,owned_ships FROM saves
                     ORDER BY id DESC
                     LIMIT 1;""").fetchall()
    if len(data) == 0:
        data = [(0,1,["yellowspaceship"])]
    return(data[0])
def save(coins,level_complete,owned_ships):
    cursy = sqlite3.connect("save.data").cursor()
    cursy.execute(f"""INSERT INTO saves(coins,level_complete,owned_ships) VALUES({coins},{level_complete},"{'/'.join(owned_ships)}");
    """)
    cursy.connection.commit()
    cursy.close()
    return