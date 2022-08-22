def mru_distance(velocity,time): 
  result = float(velocity)*float(time)
  if float(time)<0 or float(velocity)<0:
      result = 0
  context = {
    "resultado":result
  }
  return context

def mru_time(distance,velocity):
  result = distance/velocity
  if distance<0 or velocity<0:
    result = 0
  context = {
    "resultado2":result
  }
  return context

def mru_velocity(distance,time):
  result = distance/time
  if time<0 or time<0:
    result = 0
  context = {
    "resultado3":result
  }