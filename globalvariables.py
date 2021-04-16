# Variables imported from this file can be accessed in any other file that calls it, specifically helpful for the game loop.
# All of the variables declared to be None are just placeholders to be set in another file.
'''General Global Variables'''
running = True # When this becomes false, the game will close.
gamestage = "menu" # The stage that the game is in.
screen = None # The PyGame surface object for the entire game.
backgroundpicture = None # The background that is displayed.
debug = False # Gives helpful features like fps counter, useful for debugging and object placement, not for the end-user to see.
shop = None # The shop object, containing all of the functions regarding the shop.
ownedShips = ["yellowspaceship"] # List of all of the ships the player can purchase.
playercurrentship = None # The current spaceship that the player spawns with.

'''Persistant Global Variables - Loaded each time the game runs'''
lang = None # The currently selected language, read from localisation/lastlang on game initialisation.
languagesdict = None # The dictionary of all words to be used in the game, allows for the game to be adapted to non-English languages. 
coins = 0 # The number of coins the player has accumulated, read from save.data at the start of the game and saved there as the game quits. 
unlockedlevel = 1 # The highest level that the player has completed, read from save.data at the start of the game and saved there as the game quits. 

'''Level Specific Global Variables'''
leveltimer = None # The clock object that times each level.
leveltime = 0 # The number of milliseconds elapsed since the start of the level. Reset if the player respawns.

'''In-Game Sprites/Sprite Groups'''
playerspaceship = None # The spaceship that the player controls.
walls = None # All of the walls in the game.
wincondition = None # The little yellow square that you must collide with to complete the level.
spawnPoint = None # The green square that the spaceship spawns at, the starting point. 
spawnPointLocation = None # The location of the little green square mentioned above and the location at which the player spawns upon level start, or upon death. 
bullets = None # The sprite group that contains all of the bullets that have been fired.
destroyables = None # The sprite group that pertains to all of the walls that can be shot to be destroyed.
enemySpaceships = None # The sprite group that contains all of the enemy spaceships, which must be destroyed to complete the level.
optionalEnemySpaceships = None # Any enemies that can be destroyed, but don't have to be in order to complete the level.
enemyBullets = None # This contains the bullets fired by the enemies, that can destroy the player.
powerups = None # The sprite group containing all of the powerup objects.