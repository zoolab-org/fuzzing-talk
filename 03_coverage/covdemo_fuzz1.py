#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

sys.path.append('..')
from fuzzer import *
from cgidecode import *

# one round
trials = 100

seeds = [ fuzzer() for i in range(trials) ]
covs, cum = population_coverage(seeds, cgi_decode)

print(covs)
print(cum)

plt.plot(cum)
plt.title('Coverage of cgi_decode() with random inputs')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')
plt.savefig('fuzz1.pdf')
    
# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
