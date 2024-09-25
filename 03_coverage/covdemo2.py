#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')
from fuzzer import *
from cgidecode_wrapper import *

source = "cgidecode.c"

cgi_decode_wrapper('1+1')
cov1 = gcov_coverage(source)

cgi_decode_wrapper('1+%00')
cov2 = gcov_coverage(source)

print("coverage1:", cov1)
print("coverage2:", cov2)
print("** cov1 - cov2")
print(cov1 - cov2)
print("** cov2 - cov1")
print(cov2 - cov1)

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
