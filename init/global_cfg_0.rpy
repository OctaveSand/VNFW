# Here we initialize some global constants for use later in the runtime
# to check things like how much damage a given NPC does or how close to 
# starvation the MC is

# STATMAX and STATMIN are used by the entity class to check for limits (dont delete)

init python:
  STATMAX = 100
  STATMIN = 0

  THIRSTY = 30
  RTHIRSTY = 60
  DTHIRSTY = 85

  #hunger system related config
  CALORIESPERWEEK = 600
  CALORIESPERWORKOUT = 50
  HEALTHY = 90
  THIN = 70
  GAUNT = 50
  WASTED = 40
  STARVING = 30
  BEARLIKE = 90
  MUSCULAR = 70
  TONED = 50
  FIT = 40
  SCRAWNY = 30

  #injury related constants
  HURT = 40
  DYING = 80

  DAMAGE ={
    "lilly" : 5,
    "elon"  : 2,
    "erica" : 10
  }
