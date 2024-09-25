#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from z3 import *

# harder serial

s = Solver();
v = [ Int('x_'+str(i)) for i in range(20) ]
for x in v: s.add(x >= 0, x < 10)

s.add((v[15]) + (v[4]) == 10)
s.add((v[1]) * (v[18]) == 2)
s.add((v[15]) / (v[9]) == 1)
s.add((v[17]) - (v[0]) == 4)
s.add((v[5]) - (v[17]) == -1)
s.add((v[15]) - (v[1]) == 5)
s.add((v[1]) * (v[10]) == 18)
s.add((v[8]) + (v[13]) == 14)
s.add((v[18]) * (v[8]) == 5)
s.add((v[4]) * (v[11]) == 0)
s.add((v[8]) + (v[9]) == 12)
s.add((v[12]) - (v[19]) == 1)
s.add((v[9]) % (v[17]) == 7)
s.add((v[14]) * (v[16]) == 40)
s.add((v[7]) - (v[4]) == 1)
s.add((v[6]) + (v[0]) == 6)
s.add((v[2]) - (v[16]) == 0)
s.add((v[4]) - (v[6]) == 1)
s.add((v[0]) % (v[5]) == 4)
s.add((v[5]) * (v[11]) == 0)
s.add((v[10]) % (v[15]) == 2)
s.add((v[11]) / (v[3]) == 0)
s.add((v[14]) - (v[13]) == -4)
s.add((v[18]) + (v[19]) == 3)

print(s.check())

m = s.model()
print(m)
print('Serial:', ''.join([str(m[v[i]]) for i in range(len(v))]))

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
