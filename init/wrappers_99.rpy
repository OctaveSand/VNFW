init 99 python:
  import math

  ### Global wrappers and convienence functions 
  # These are the last thing initialized (99) and are only intended for writers
  # to use from within Labels.

  def achievement_get(name, d=''):
    #flags player for the named achievement, notifies them via the ui, and kicks off automation
    f = name.lower()
    ePLAYER.set_flag(f)
    if(d == ''):
      d = "Achievement get!: {}".format(name)
    renpy.say(achievement, d)
    #check for automation
    if(name in ACHIEVEMENTS):
      ACHIEVEMENTS[name].run()


  def achievement_has(name):
    #returns true if player has the named achievement
    if(ePLAYER.is_flagged(name)):
      return True
    return False


  def gain_status(name, d=''):
    #flags player for flag_name and notifies them via the ui
    f = name.lower()
    ePLAYER.inc_counter(f)
    if(not check_flag(f)):
      ePLAYER.set_flag(f)
      if(d == ''):
        d = name.upper()
      renpy.say(statgain,d)


  def lose_status(name, d=''):
    #un-flags player for flag_name and notifies them via the ui
    f = name.lower()
    if(check_flag(f)):
      ePLAYER.rm_flag(f)
      if(d == ''):
        d = name.upper()
    renpy.say(statlose,d)


  def inc_stat(stat_name, d='', v = 1):
    #a wrapper for ePLAYER.ding() that optionally notifies the player via ui
    inc = ePLAYER.ding(stat_name,v)
    if(d != ''):
      renpy.say(stat_increase,d)
    else:
      renpy.say(stat_increase,"you've gained {}".format(stat_name))


  def ding(stat_name, d='', v = 1):
    #a wrapper for ePLAYER.ding() that optionally notifies the player via ui
    inc = ePLAYER.ding(stat_name,v)
    if(d != ''):
      renpy.say(stat_increase,d)
    else:
      renpy.say(stat_increase,"you've gained {}".format(stat_name))


  def injury(who, where, v=0):
    #raises the players injury stat, notifies player via ui
    msg = "Careful! {} has damaged your {}".format(who,where)
    if v > 0:
      ePLAYER.inc_stat("injury",v)
    elif(who in DAMAGE):
      ePLAYER.inc_stat("injury",DAMAGE[who])
    else:
      d = renpy.random.randint(1,10)
      ePLAYER.inc_stat("injury",d)
    renpy.say(injurygain, msg)


  def inc_multiplier(name, d='', v = 1):
    #increase a multiplier
    inc = ePLAYER.inc_multiplier(name,v)
    if(d == ''):
      d = "From now on, you will be more susceptable to {}".format(name)
    renpy.say(multiplier_increase,d)


  def dec_multiplier(name, d='', v = 1):
    #decrease a multiplier
    inc = ePLAYER.dec_multiplier(name,v)
    if(d == ''):
      d = "You feel less affected by {}".format(name)
    renpy.say(multiplier_decrease,d)


  def dec_stat(stat_name, d='', v = -1):
    #decrease a stat
    if(v > 0):
      v = (v*-1) 
    dec = ePLAYER.ding(stat_name,v)
    if(d == ''):
      d = "-{} {}".format(dec,stat_name)
    #renpy.say(stat,d)


  def reset_stat(stat_name):
    ePLAYER.set_stat(stat_name,STATMIN)


  def half_stat(stat_name):
    s = math.ceil(ePLAYER.get_stat(stat_name))
    ePLAYER.set_stat(stat_name,(s/2))


  def toggle(name):
    if(ePLAYER.is_flagged(name)):
      ePLAYER.rm_flag(name)
    else:
      ePLAYER.set_flag(name)


  def check_flag(name):
    return ePLAYER.is_flagged(name)


  def clear_flag(name):
    ePLAYER.rm_flag(name)

    
  def set_flag(name):
    ePLAYER.set_flag(name)


  def flag(name):
    ePLAYER.set_flag(name)


  def enable_event(name):
    #enable an event
    EVENTS[name].enable()


  def disable_event(name):
    #enable an event
    EVENTS[name].disable()

  def event_enabled(name):
    return EVENTS[name].v['enabled']


  def enable_interaction(name):
    #enable an event
    INTERACTIONS[name].enable()


  def disable_interaction(name):
    #enable an event
    INTERACTIONS[name].disable()


  def interaction_enabled(name):
    return INTERACTIONS[name].v['enabled']


  def motd_doesnt_have(substring):
    for message in MOTD:
      if(substring in message):
        return False
    return True


  def motd_replace(substring, string):
    for key,replace_me in enumerate(MOTD):
      if (substring in replace_me):
        del(MOTD[key])
    MOTD.append(string)


  def wearing(a):
    return ePLAYER.is_wearing(a)


  def describe_article(t):
    return ePLAYER.describe_article(t)


  def take_off_and_give(a):
    #take off an article of clothing and give it away
    article = ePLAYER.get_article(a)
    ePLAYER.take_off(a)
    ePLAYER.take(article.uid)

  def strip():
    for a in ePLAYER.wearing:
      if(a.category == "clothing"):
        ePLAYER.take_off(a)
        renpy.say(None,"You take off your {}".format(a.name))


  def pay(n,who):
    c = (n/100)
    ePLAYER.pay(n)
    renpy.say(None, "You paid {} credits to {}".format(c,who))


  def earn(n):
    c = (n/100)
    ePLAYER.earn(n)
    renpy.say(None, "You earned {} credits!}".format(c))


  def reset_hunger():
    lose_status('starvation')
    lose_status('really_hungry','Really Hungry')
    lose_status('hungry')

  def reset_thirst():
    lose_status('thirsty')
    lose_status('really_thirsty','Really Thirsty')
    lose_status('extreme_thirst','Extremely Thirsty')


  def inc_counter(n):
    ePLAYER.inc_counter(n)


  def get_count(n):
    ePLAYER.get_count(n)


  def set_health():
    H = ePLAYER.get_stat('calories')
    if( H > HEALTHY):
      ePLAYER.set_attribute('health',"Healthy")
    elif( H > THIN ):
      ePLAYER.set_attribute('health',"Thin")
    elif( H > GAUNT ):
      ePLAYER.set_attribute('health',"Gaunt")
    elif( H > WASTED ):
      ePLAYER.set_attribute('health',"Wasted")
    elif( H > STARVING ):
      ePLAYER.set_attribute('health',"Starving")


  def set_physique():

  print "game init done" 
