#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..');
from fuzzer import *

seed = "http://www.google.com/search?q=fuzzing"
trials = 50

inp = seed
for i in range(trials):
    if i % 5 == 0: print(i, "mutations:", repr(inp))
    inp = mutate(inp)

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
