# The script of the game goes in this file.

# These character definitions are for the Renpy framework
# main character
define you = Character("You")
image you  = Placeholder("boy")

# An npc
define l = Character("Lilly")
image l  = Placeholder("girl")

#Some convienience blank screens
image black = "#000000"
image grey = "#D3D3D3"


# DONT TOUCH: These are fake character defs for use with shiny alert messages 
define statgain = Character("You have gained the status:", color="#009900", what_color="#009900")
define statlose = Character("You have lost the status:", color="#009900", what_color="#009900" )
define stat_increase = Character("Stat Increase", color="#009900", what_color="#009900")
define stat_decrease = Character("Stat Decrease", color="#009900", what_color="#009900")
define multiplier_increase = Character("Multiplier Increased", color="#009900", what_color="#009900")
define multiplier_decrease = Character("Multiplier Decreased", color="#009900", what_color="#009900")
define injurygain = Character("You have sustained an injury:", color="#990000", what_color="#990000" )
define achievement = Character("Achievement Get!:", color="#009900", what_color="#009900")
define caloricdef = Character("You didn't consume enough calories this week!", color="#990000", what_color="#990000" )

#reset the game and player objects (in case of restarts)
python:
  DEBUG = True
  GAME.reset()
  ePLAYER.flags = {}
  ePLAYER.attributes = {}
  ePLAYER.stats = {}
  ePLAYER.inventory = {} 
  ePLAYER.wearing = {} 
  ePLAYER.set_stat('hunger',10)   
  ePLAYER.set_stat('lust',0) 
  ePLAYER.wear( Wearable('shirt', 'shirt', 'plain t-shirt' ))
  ePLAYER.wear( Wearable('jeans', 'pants', 'blue-jeans' ))
  ePLAYER.wear( Wearable('flag boxers', 'underwear', 'heart-print boxers' ))

# The game starts here.
label start:
  $MOTD.append("Welcome! Sucka")

  ### Proper startup 
  jump intro

  ### or uncomment for Debugging startup
  #$GAME.fast_forward(3)
  #jump three_days_in
