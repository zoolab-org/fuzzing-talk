#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from z3 import *

puzzle = ((0,0,0,0,9,4,0,3,0),
          (0,0,0,5,1,0,0,0,7),
          (0,8,9,0,0,0,0,4,0),
          (0,0,0,0,0,0,2,0,8),
          (0,6,0,2,0,1,0,5,0),
          (1,0,2,0,0,0,0,0,0),
          (0,7,0,0,0,0,5,2,0),
          (9,0,0,0,6,5,0,0,0),
          (0,4,0,9,7,0,0,0,0))

s = Solver()
v = [ [ Int('x'+str(i)+str(j)) for i in range(9) ]
        for j in range(9) ]

[ s.add(1 <= v[y][x], v[y][x] <= 9) for y in range(9) for x in range(9) ]
[ s.add(Distinct(v[y])) for y in range(9) ]
[ s.add(Distinct([ v[y][x] for y in range(9) ])) for x in range(9) ]
[ s.add(Distinct([ v[3*y + dy][3*x + dx] for dy in range(3) for dx in range(3) ]))
            for y  in range(3) for x  in range(3) ]
[ s.add(If(puzzle[i][j] == 0, True, v[i][j] == puzzle[i][j]))
            for i in range(9) for j in range(9) ]

if s.check() == sat:
    m = s.model();
    r = [ ''.join([ str(m.evaluate(v[i][j])) for j in range(9) ]) for i in range(9) ]
    print('\n'.join(r))
else:
    print("cannot solve")

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
