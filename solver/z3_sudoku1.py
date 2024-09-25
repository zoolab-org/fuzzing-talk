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

c_cell = [ And(1 <= v[i][j], v[i][j] <= 9) for i in range(9) for j in range(9) ]
c_rows = [ Distinct(v[i]) for i in range(9) ]
c_cols = [ Distinct([ v[i][j] for i in range(9) ]) for j in range(9) ]
c_sqr  = [ Distinct([ v[3*i0 + i][3*j0 + j]
             for i in range(3) for j in range(3) ])
             for i0 in range(3) for j0 in range(3) ]

c_puzzle = [ If(puzzle[i][j] == 0,
             True, v[i][j] == puzzle[i][j]) for i in range(9) for j in range(9) ]

s.add(c_cell + c_rows + c_cols + c_sqr + c_puzzle)

if s.check() == sat:
    m = s.model();
    r = [ ''.join([ str(m.evaluate(v[i][j])) for j in range(9) ]) for i in range(9) ]
    print('\n'.join(r))
else:
    print("cannot solve")

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
