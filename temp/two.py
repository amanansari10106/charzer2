from math import acos, sin, cos, radians, degrees

from typing import DefaultDict
from sympy import symbols, solve
import sympy
slat = radians(21.208998)
slon = radians(81.377907)
elon = radians(81.324194)
elat = radians(21.201257)
# elon = slon
# elat = slat
z = sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon)
# dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
dist = 6371.01 * acos(z)
# dist = acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
# cos(dist/6371.01)-sin(slat)*sin(elat) = cos(slat)*cos(elat)*cos(slon - elon)
# (cos(dist/6371.01)-sin(slat)*sin(elat))/cos(slat)*cos(elat) = cos(slon - elon)

# print(dist)
# dist = 50

# x = symbols('x')
# a = 6371.01 * acos(sin(slat)*sin(elat))
# b= cos(slat)*cos(elat)
# # e = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
# # expr = (6371.01 * sympy.acos(sympy.sin(slat)*sympy.sin(elat) + sympy.cos(slat)*sympy.cos(elat)*sympy.cos(x))) - dist
# expr = (a + b*sympy.cos(x))-dist

# sol = solve(expr)
# print(sol)
a = cos(dist/6371.01)-sin(slat)*sin(elat)
b= cos(slat)*cos(elat)
c= a/b

dif = acos((cos(dist/6371.01)-sin(slat)*sin(elat))/cos(slat)*cos(elat))
dif = acos(c)
z=degrees(slon)
perdif = abs(elon-slon)
print(abs(dif))
print(perdif)
print(z)

if dif>0:
    rlon = slon - dif
    pass
elif dif<0:
    rlon = slon + dif
    pass





# print(dist)

slat = radians(21.208998)
slon = radians(81.377907)
elat = slat

dist = 50
a = cos(dist/6371.01)-sin(slat)*sin(elat)
b= cos(slat)*cos(elat)
c= a/b


# re = device.objects.raw('SELECT id, ( 3959 * acos( cos( radians(37) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians(-122) ) + sin( radians(37) ) * sin( radians( lat ) ) ) ) AS distance FROM markers HAVING distance < 25 ORDER BY distance LIMIT 0 , 20;')

# a = (3959 * acos( cos( radians(elat) ) * cos( radians( slat ) ) * cos( radians( slon ) - radians(elon) ) + sin( radians(elat) ) * sin( radians( slat ) ) ) )
# print(a)