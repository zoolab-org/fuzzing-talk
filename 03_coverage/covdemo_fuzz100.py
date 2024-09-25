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
runs = 100
cum_sum = [0] * trials
for _ in range(runs):
    seeds = [ fuzzer() for i in range(trials) ]
    cov, cum = population_coverage(seeds, cgi_decode)
    for i in range(trials): cum_sum[i] += cum[i]

cum_avg = [ x / runs for x in cum_sum ]

plt.plot(cum_avg)
plt.title('Average coverage of cgi_decode() with random inputs')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')
plt.savefig('fuzz100.pdf')
    
# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
