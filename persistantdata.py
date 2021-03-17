import sqlite3
cursy = sqlite3.connect("save.data").cursor()
cursy.execute("""CREATE TABLE IF NOT EXISTS saves (
                    id integer PRIMARY KEY,
                    coins integer NOT NULL,
                    level_complete integer NOT NULL
                );
""")
cursy.close()
def load():
    cursy = sqlite3.connect("save.data").cursor()
    data = cursy.execute("""SELECT coins,level_complete FROM saves
                     ORDER BY id DESC
                     LIMIT 1;""").fetchall()
    if len(data) == 0:
        data = [(0,1)]
    return(data[0])
def save(coins,level_complete):
    cursy = sqlite3.connect("save.data").cursor()
    cursy.execute(f"""INSERT INTO saves(coins,level_complete) VALUES({coins},{level_complete});
    """)
    cursy.connection.commit()
    cursy.close()
    return