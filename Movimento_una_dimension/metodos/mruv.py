def mruv_vf1(v0,a,t):
  return v0+(a*t)

def mruv_d1(v0,t,a):
  return (v0*t)+((a*pow(t,2))/2)

def mruv_d2(vf,v0,t):
  return ((vf+v0)/2)*t

def mruv_vf2(v0,a,d):
  return math.sqrt(pow(v0,2)+(2*a*d))