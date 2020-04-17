init 10 python:

  '''
    class thingy defines things that can be stored in player inventory
    multipliers/flags are not yet implemented
  ''' 

  class Thingy(object):
    def __init__(self, name, desc, type = 'thingy', flags=[], m=[], v={}):
      self.uid = renpy.random.random()
      self.name = name # short human-readable description "dildo"
      self.desc= desc # the description output by the stats ui "a large black dildo"
      self.type= type # item type: 'dildos'
      self.flags = flags  # flags conferred by this wearable
      self.multipliers = m # multipliers conferred by this wearable
      self.v = v #ad-hoc values [color: black, length: 15in]
