#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

sys.path.append('..')
from fuzzer import *
from cgidecode_wrapper import *

runs = 100
trials = 100
program = './cgidecode'
source  = 'cgidecode.c'

# one round
trials = 100
runs = 100
cum_sum = [0] * trials
for _ in range(runs):
    cum_cov = []
    all_cov = set()
    seeds = [ fuzzer() for i in range(trials) ]
    for s in seeds:
        cgi_decode_wrapper(s)
        cov = gcov_coverage(source)
        all_cov |= cov
        cum_cov.append(len(all_cov))
        print('.', end='');
    for i in range(trials): cum_sum[i] += cum_cov[i]
    print(_);

cum_avg = [ x / runs for x in cum_sum ]

plt.plot(cum_avg)
plt.title('Average coverage of cgi_decode() with random inputs')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')
plt.savefig('ext100.pdf')

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
