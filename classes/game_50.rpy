'''
  The game class controls the passage of time and turn events, and runs `event` 
  automation. The TIMES data structures control how many turns there are in a day,
  and may be extended or truncated as desired (by default there are 5 turns per day).
  Call GAME.end_day() to end the current day, GAME.end_turn() to move the clock one turn
  (this automatically shifts the day/week if required)
  A call to GAME.home() sets the screen to the current GAME.location and returns control to the player
'''

init 50 python:
  class Game(object):
    def __init__(self,location, player):
      self.player = player
      self.flags = {} # a dict of boolean values (gino_alive : true)
      self.attributes = {} # a dict of strings  (beer_quality:good)
      self.location = location # a string representing the current location's name 
      
      self.DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
      self.rDAYS = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
      self.TIMES = ["Morning","Noon","Evening","Night","Late"]
      self.rTIMES = {"Morning":0,"Noon":1,"Evening":2,"Night":3,"Late":4}

      #event queues
      self.events_scheduled = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[],"Sunday":[]}
      self.events_fired = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[],"Sunday":[]}
      self.julian_queue = {} # an array of class/event whose index cooresponds to game.jday
  
      #time/turn attributes
      self.turn = 0
      self.day = 0
      self.time = self.TIMES[self.turn] #morning
      self.today = self.DAYS[self.day] #monday
      self.week = 0
      self.jday = 1 #julian day
      self.yesterday = self.DAYS[6] # sunday
      self.tomorrow = self.DAYS[1]  # tuesday

  
    def set_attr(name,v):
      self.attributes[name] = v
  
  
    def get_attr(name):
      if(name in self.attributes):
        return self.attributes[name]
      else:
        return None
  
  
    def set_flag(name,v=True):
      self.flags[name] = v
  
  
    def is_flagged(name):
      if(name in self.flags):
        return self.flags[name]
      else:
        return False
  
  
    def rm_flag(name):
      return self.flags.pop(name,None)
  

    def home(self):
      #process all time-based events and turn control back to the current location
      self.process_events()
      renpy.jump(self.location)


    def set_location(self,loc):
      # reset the current location 
      self.location = loc
  
      #check this location's queue for pending, runnable interactions
      for e in ENTITIES[loc].Q:
        if( e.is_runnable()):
          renpy.jump(e.label)
  
  
    def process_events(self):
      #process the DOW queue first
      for k,job in enumerate(self.events_scheduled[self.today]):
        if(job.v['location'] in ['any',self.location]):
          if(job.is_runnable()):
            self.events_fired[self.today].append(self.events_scheduled[self.today].pop(k))
            job.v['last_fired']=[self.jday,self.day,self.time]
            job.run()
      #Then process the julian-scheduled events
      if self.jday in self.julian_queue:
        for k,job in enumerate(self.julian_queue[self.jday]):
          if(job.v['location'] in ['any',self.location]):
            if(job.is_runnable()):
              self.julian_queue[self.jday].pop(k)
              job.v['last_fired']=[self.jday,self.day,self.time]
              job.run()
          

    def reset_events(self):
      #reschedule todays jobs for next week
      for e in self.events_fired[self.today]:
        self.events_scheduled[self.today].append(e)
      self.events_fired = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[],"Sunday":[]}

    def end_turn(self):
      if(self.turn >= len(self.TIMES)):
        self.end_day()
      else:
        self.reset_events()
        self.turn += 1
        self.time = self.TIMES[self.turn] #morning
        self.home()
  
    def end_day(self):
      self.reset_events()
      # do all the date munging
      self.yesterday = self.today
      self.turn = 0
      self.time = self.TIMES[self.turn] #morning
      self.day += 1
      self.jday += 1
  
      if(self.day == len(self.DAYS)):
        self.week += 1
        self.day = 0
  
      self.today = self.DAYS[self.day] #monday
      if(self.day == len(self.DAYS)-1):
        self.tomorrow = 0
      else:
        self.tomorrow = self.DAYS[self.day+1]
  
      renpy.jump("end_day")

    def fast_forward(self,days):
      #fast-forward the game day without processing events or calling end_day
      self.reset_events()
      self.turn = 0
      for n in range(days):
        self.yesterday = self.today
        self.time = self.TIMES[self.turn] #morning
        self.day += 1
        self.jday += 1
        if(self.day == len(self.DAYS)):
          self.week += 1
          self.day = 0
  
        self.today = self.DAYS[self.day] #monday
        if(self.day == len(self.DAYS)-1):
          self.tomorrow = 0
        else:
          self.tomorrow = self.DAYS[self.day+1]
  

    def reset(self):
      self.flags = {} # a dict of boolean values (gino_alive : true)
      self.attributes = {} # a dict of strings  (beer_quality:good)
      self.location = "cell"
      self.turn = 0
      self.day = 0
      self.time = self.TIMES[self.turn]
      self.today = self.DAYS[self.day]
      self.week = 0
      self.jday = 1 #julian day
      self.yesterday = self.DAYS[6]
      self.tomorrow = self.DAYS[1]
