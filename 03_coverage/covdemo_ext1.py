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

program = './cgidecode'
source  = 'cgidecode.c'

# one round
trials = 100
all_cov = set();
cum_cov = [];
seeds = [ fuzzer() for i in range(trials) ]
for s in seeds:
    cgi_decode_wrapper(s);
    cov = gcov_coverage(source)
    all_cov |= cov
    cum_cov.append(len(all_cov))

print(all_cov)
print(cum_cov)

plt.plot(cum_cov)
plt.title('Average coverage of cgi_decode() with random inputs')
plt.xlabel('# of inputs')
plt.ylabel('lines covered')
plt.savefig('ext1.pdf')

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
