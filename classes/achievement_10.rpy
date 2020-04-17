init 10 python:

  '''
    The achievement class defines automation that runs when the player gains an achievement
    achievements are run by evoking their .run() method, and may or may not branch to a label
  '''
  ACHIEVEMENTS = {} # global achievement-objects dict

  class Achievement(object):
    def __init__(self, name,v={}):
      self.name = name
      self.v = v
      ACHIEVEMENTS[name] = self


    def run(self):
      return True
