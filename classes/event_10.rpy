init 10 python:

  '''
    The event class defines automation that runs at timed intervals 
    They may be scheduled based on the day-of-the-week (DOW) or by julian day.
    Hence, events are always run by the GAME object on end_turn() / end_day() calls, by 
    invoking the event's .run() method. 
  ''' 

  EVENTS = {} # global events dict

  class Event(object):
    def __init__(self, name, type, days=[], v={"enabled":False, "location":"cell"}):
      self.name = name
      self.type = type
      self.v = v #ad-hoc variables
      self.days = days
      EVENTS[name] = self

    def schedule(self,GAME):
      # where to schedule this event in the game queues
      if(self.type == "jday"):
        #julian-date based scheduling
        for d in self.days:
          if d in GAME.julian_queue:
            GAME.julian_queue[d].append(self)
          else:
            GAME.julian_queue[d] = [self]
      else:
        #DOW based scheduling
        if 'any' in self.days:
          for d in GAME.DAYS:
            GAME.events_scheduled[d].append(self)
        else:
          for d in self.days:
            GAME.events_scheduled[d].append(self)


    def is_runnable(self):
      return self.v['enabled']


    def run(self):
      return True


    def enable(self):
      self.v["enabled"] = True


    def disable(self):
      self.v["enabled"] = False
