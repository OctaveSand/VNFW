# locations are just a label that shows the appropriate screens
# The call to GAME.set_location() causes the game to check the global ENTIIES struct
# for an entity called "cell", if it finds one, it'll recurse through that entitie's
# interactions queue, running any interactions it finds. 

label cell:
  $GAME.set_location("cell")
  show screen hud
  call screen cell
