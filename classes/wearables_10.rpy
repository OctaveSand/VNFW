init 10 python:

  
  #class wearable defines objects that can be worn

  valid_wearable_types = {'shirt':'shirt',
                          'pants':'pants',
                          'socks':'socks',
                          'shoes':'shoes',
                          'underwear':'underwear', 
                          'undershirt':'undershirt',
                          'hat': 'hat',
                          'gag': 'gag',
                          'necklace':'necklace', 
                          'collar':'collar', 
                          'glasses': 'glasses',
                          'earrings': 'earrings',
                          'nosepiercing': 'nosepiercing',
                          'lippiercing': 'lippiercing',
                          'tonguepiercing': 'tonguepiercing',
                          'nipplepiercing': 'nipplepiercing',
                          'bellypiercing': 'bellypiercing',
                          'cockring': 'cockring',
                          'strapon': 'strapon',
                          'buttplug': 'buttplug',
                          'cockpiercing':'cockpiercing'}

  class Wearable(Thingy):
    def __init__(self, name, type, desc, flags=[], m=[], category='clothing', v={"removable":True}):
      self.uid = renpy.random.random()
      self.name = name # short human-readable description "Lillys Collar"
      #intentionally panic if type not in valid_wearable_types
      self.type = valid_wearable_types[type] # type of wearable (shirt, collar, buttplug etc..)
      self.category = category # clothing or jewelry
      self.desc= desc # the description output by the stats ui "a rose-colored collar enscribed: `Lillys Bitch`"
      self.flags = flags  # flags conferred by this wearable
      self.multipliers = m # multipliers conferred by this wearable
      self.v = v #ad-hoc values [color: rose, weight: 5oz]
