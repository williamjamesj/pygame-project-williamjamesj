import sqlite3
cursy = sqlite3.connect("save.data").cursor()
cursy.execute("""CREATE TABLE IF NOT EXISTS saves (
                    id integer PRIMARY KEY,
                    coins integer NOT NULL,
                    level_complete integer NOT NULL,
                    owned_ships TEXT NOT NULL,
                    playercurrentship TEXT NOT NULL,
                    musicvol integer NOT NULL,
                    sfxvol integer NOT NULL
                );
""")
cursy.close()
def load():
    cursy = sqlite3.connect("save.data").cursor()
    data = cursy.execute("""SELECT coins,level_complete,owned_ships,playercurrentship,musicvol,sfxvol FROM saves
                     ORDER BY id DESC
                     LIMIT 1;""").fetchall()
    if len(data) == 0:
        data = [(0,1,"yellowspaceship","yellowspaceship/10/0.1/3/1/0/1/0",10,10)]
    return(data[0])
def save(coins,level_complete,owned_ships,playercurrentship,musicvol,sfxvol):
    cursy = sqlite3.connect("save.data").cursor()
    cursy.execute(f"""INSERT INTO saves(coins,level_complete,owned_ships,playercurrentship,musicvol,sfxvol) VALUES({coins},{level_complete},"{'/'.join(owned_ships)}","{'/'.join(playercurrentship)}",{musicvol},{sfxvol});
    """)
    cursy.connection.commit()
    cursy.close()
    return