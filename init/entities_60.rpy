init 60 python:
  # ENtity creation

  ####### CHARACTERS 
  # first declare the player entity, (she must ALWAYS be called ePLAYER)
  # Note her default label: `home`. every entity needs a home label, but in the player's
  # case it's probably a bug if the home label is ever actually called
  ePLAYER = Entity('player','home')

  # Now we can set some stats on her and give her clothes
  ePLAYER.set_stat('thirst',0)    # at STATMAX you are dead of dehydration
  ePLAYER.set_stat('lust',10)   # at STATMAX you are dead of starvation
  ePLAYER.wear( Wearable('shirt', 'shirt', 'plain t-shirt' ))
  ePLAYER.wear( Wearable('jeans', 'pants', 'blue-jeans' ))
  ePLAYER.wear( Wearable('boxers', 'underwear', 'heart-print boxers' ))

  # Here's an example NPC, she can be named anything and doesn't require stats or clothes
  # but her home label must exist
  eLILLY = Entity('lilly','lilly_home')

  ####### LOCATIONS
  # Entites aren't just for people. Generally anything that can be interacted can be
  # modeled as an entity. Here's a jail cell
  
  eROOM = Entity('cell','cell')
  eROOM.description = 'A Cell'

  ####### OBJECTS
  # And here's some stuff inside the cell we can interact with
  eCELL_DOOR = Entity('cell_door','cell_door')
  eCELL_TV = Entity('cell_tv','cell_tv')
  eCELL_TOILET = Entity('cell_toilet','cell_toilet')
  eCELL_SHELF = Entity('cell_shelf','cell_shelf')
  eCELL_BED = Entity('cell_bed','cell_bed')


  print "entities init done"
