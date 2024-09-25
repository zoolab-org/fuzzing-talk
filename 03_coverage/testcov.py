#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')
from fuzzer import *

trace = []
coverage_enable(trace);
print('aaa');
print('bbb');
coverage_disable();

print(trace);

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
