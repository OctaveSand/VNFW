init 10 python:

  '''
    The interactions class defines automation that runs when a use clicks on an entity.
    Every entity has an `interact()` method, and a Queue which stores interaction objects.
    When the user clicks on/interacts with an entity (usually via an imagemap), the 
    queue is checked for runnable interactions. If none are found the player is jumped to
    that entites "home" label.
    Interactions also run on calls to GAME.set_location() when the player changes locations
    in the game.
  ''' 

  INTERACTIONS = {} # global interactions dict

  class Interaction(object):
    def __init__(self, label, entity_name, v={}):
      self.label = label # the rpy label this event launches
      self.v = v #ad-hoc variables
      ENTITIES[entity_name].Q.append(self) # register the interaction with the entity's queue
      INTERACTIONS[label] = self #register with the global index of interactions

      
    # override this method to set specific requirements 
    def is_runnable(self):
      if 'enabled' in self.v:
        return self.v['enabled']
      else:
        return False

    def enable(self):
      self.v['enabled'] = True

    def disable(self):
      self.v['enabled'] = False
