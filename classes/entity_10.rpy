init 10 python:

  '''
    The entity class is a variable bucket that holds various types of values for
    the in-game entities like characters and locations. It comes with a global
    dictionary which automatically registers new entities with the global dict
    for easy lookup later 
  ''' 
  
  #global entities dict
  ENTITIES = {}

  #entity class
  class Entity(object):
    def __init__(self, name, label):
      self.name = name
      self.label = label
      self.pname = name # a pretty-printed description of the entity
      self.description = name # a rollover-style description of the entity
      self.flags = {} # a dict of boolean values (anal_virgin:true)
      self.counters = {} # a dict of counters (anus_penetrated:999)
      self.attributes = {} # a dict of strings  (hair:brown)
      self.stats = {} #a dict of integer values (strength:10)
      self.multipliers = {} #stat multiplier values
      self.inventory = {} #a dict of class/thingy indexed by uid
      self.wearing = {} #a dict of class/wearables indexed by type
      self.honorifics = {} # a dict of strings representing honorifics (lilly:mistress)
      self.v = {} # a just-in-case dict of temporary adhoc values (thingIdidntThinkOf:True)
      self.credits = 0 # money
      self.Q = [] # this entity's interaction queue

      #register the entity with the global entites stuct for lookups
      ENTITIES[self.name] = self 

    def delete(self):
      return ENTITIES.pop(self.name, None)

    ### Flag methods
    def set_flag(self, name,v=True):
      self.flags[name] = v

    def is_flagged(self, name):
      if(name in self.flags):
        return self.flags[name]
      else:
        return False

    def rm_flag(self, name):
      return self.flags.pop(name,None)

    ### Attribute methods
    def set_attr(self, name, v):
      self.attributes[name] = v

    def get_attr(self, name):
      if(name in self.attributes):
        return self.attributes[name]
      else:
        return None


    ### Counter methods
    def inc_counter(self, name,v=1):
      if name in self.counters:
        self.counters[name] += v
      else:
        self.counters[name] = v

    def get_count(self, name):
      if name in self.counters:
        return self.counters[name]
      return 0


    ### Stat methods
    def set_stat(self, name,v=0):
      self.stats[name] = v

    def inc_stat(self, name,v=1,m=STATMAX):
      if name in self.stats:
        self.stats[name] += v
      else:
        self.stats[name] = v

      if(self.stats[name] > m):
        self.stats[name] = m

    def dec_stat(self, name,v=1, m=0):
      if name in self.stats:
        self.stats[name] -= v
      else:
        self.stats[name] = v
      if(self.stats[name] < m):
        self.stats[name] = m

    def get_stat(self, name):
      if(name in self.stats):
        return self.stats[name]
      else:
        return None 

    def set_multiplier(self, name, v=2):
      self.multipliers[name]=v

    def get_multiplier(self, name):
      if(name not in self.multipliers):
        self.multipliers[name]=1
      return self.multipliers[name]

    def inc_multiplier(self, name, v=1):
      if(name not in self.multipliers):
        self.multipliers[name] = v
      else:
        self.multipliers[name] += v

    def dec_multiplier(self, name, v=1):
      if(name not in self.multipliers):
        self.multipliers[name] = 1
      else:
        if(self.multipliers[name] > 1):
          self.multipliers[name] -= v
        else:
          self.multipliers[name] = 1


    def ding(self, name, v=1, m=STATMAX):
    # ding is the primary stat interface. it takes into account the stat multipliers
      if(name not in self.stats):
        self.stats[name]=0
      if(name not in self.multipliers):
        self.multipliers[name]=1
      increase_value = (self.multipliers[name] * v)
      self.stats[name] += increase_value
      if(self.stats[name] >= m):
        self.stats[name] = m
      return increase_value


    ### Inventory methods
    def give(self, item):
      #item is a class/thingy
      self.inventory[item.uid] = item
      
    def take(self, uid ,v=1):
      if(uid in self.inventory):
        del(self.inventory[uid])

    ### clothes
    def wear(self, w):
      # remove wearable from inventory and add to self.wearing
      #w is a wearable
      #wearable class defined in class/wearables
      for m in w.multipliers:
        self.inc_modifier[m]
      for f in w.flags:
        self.set_flag[f]
      self.set_flag("wearing_%s".format(w.type))
      if w.type in self.wearing:
        self.take_off(w.type)
      self.wearing[w.type] = w


    def get_uids_by_name(self, n):
      #search inventory for thingies with name n and return their uids
      #this may return more than one result or an empty array
      out = []
      for uid,thingy in enumerate(self.inventory):
        if(thingy.name == n):
          out.append(uid)
      return out


    def describe_article(self, t):
      #return the description of the wearable in the t slot
      #intentionally panic if t isn't in self.wearing
        return self.wearing[t].desc


    def describe_thingy(self, u):
      #return the description of the thingy with uid u
      #intentionally panic if u isn't in self.inventory
        return self.inventory[u].desc


    def get_article_uid(self,t):
      #return the uid of the wearable in slot t
      #intentionally panic if t isn't in self.wearing
        return self.wearing[t].uid


    def is_wearing(self, t):
      #return true if there is a wearable in the t slot
      if t in self.wearing:
        return True
      return False

    def is_naked(self):
      #return true if the player is naked
      for article in e.PLAYER.wearing:
        if article.category == 'clothing':
          return False
      return True


    def take_off(self, t):
      # remove wearable from self.wearing and add to self.inventory
      #t is a wearable type (like 'shirt')
      #intentionally panic if t isn't in self.wearing
      for m in self.wearing[t].multipliers:
        self.dec_modifier[m]
      for f in self.wearing[t].multipliers:
        self.rm_flag[f]  # this is a bug if the flag is also set by something else
      self.rm_flag("wearing_{}".format(t))
      self.give(self.wearing.pop(t))


    ### honorific methods
    def set_title(self, name,title):
      self.honorifics[name] = title


    def get_title(self, name):
      if(name in self.honorifics):
        return self.honorifics[name]
      else:
        self.set_title(name,name)
        return self.honorifics[name]


    ### money-related methods
    def earn(self,n):
      # make money
      self.credits += n

    def pay(self,n):
      # lose money
      if(self.credits > n):
        self.credits -= n
      else:
        self.credits = 0


    ### Queue-related methods
    def interact(self):
      #process this entities queue and foward them to the default label if no interactions are found
      for interaction in self.Q:
        if(interaction.is_runnable()):
          renpy.jump(interaction.label)

      #We didn't find any waiting events, so go ahead and jump to this entities default label
      renpy.jump(self.label)
