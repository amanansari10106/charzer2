from math import acos, sin, cos, radians, degrees
# from typing import DefaultDict

slat = radians(21.208998)
slon = radians(81.377907)
elat = slat

dist = 50
a = cos(dist/6371.01)-sin(slat)*sin(elat)
b= cos(slat)*cos(elat)
c= a/b
dif = abs(acos(c))

rlon1 = slon +dif
rlon2 = slon - dif

from haversine import haversine, Unit

lyon = (21.208965, 81.377884) # (lat, lon)
paris = (22.208965, 81.377884)

a = haversine(lyon, paris)
print(a)