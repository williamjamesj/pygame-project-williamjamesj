import sqlite3
cursy = sqlite3.connect("save.data").cursor()
cursy.execute("""CREATE TABLE IF NOT EXISTS saves (
                    id integer PRIMARY KEY,
                    save_name text NOT NULL,
                    coins integer NOT NULL,
                    level_complete integer NOT NULL
                );
""")
