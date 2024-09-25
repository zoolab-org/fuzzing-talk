#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')
from fuzzer import *
from cgidecode import *

#trace = [];
#coverage_enable(trace);
#cgi_decode('1+1');
#coverage_disable();

with Coverage() as cov1: cgi_decode('1+1');
with Coverage() as cov2: cgi_decode('1+%00');

print("coverage1:", cov1.coverage());
print("coverage2:", cov2.coverage());
print("** cov1 - cov2");
print(cov1.coverage() - cov2.coverage());
print("** cov2 - cov1");
print(cov2.coverage() - cov1.coverage());

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
