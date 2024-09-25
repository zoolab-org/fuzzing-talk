#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

sys.path.append('..');
from fuzzer import *

trials = 1000
program = "bc"

FILE, DIR = get_tempfile();
#print("FILE:", FILE)

runs = []
for i in range(trials):
    data = fuzzer();
    open(FILE, 'w').write(data);
    result = run([program, FILE]);
    runs.append((data, result))

## show all errors
#print('\n'.join([result.stderr for (data, result) in runs if result.stderr != '']))

## show all errors except 'illegal character' and 'syntax error'
print('\n'.join([result.stderr for (data, result) in runs if result.stderr != '' and "illegal character" not in result.stderr and "syntax error" not in result.stderr]))

os.remove(FILE)
os.removedirs(DIR)

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
