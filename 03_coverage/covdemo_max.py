#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')
from fuzzer import *
from cgidecode import *

with Coverage() as covmax:
    cgi_decode('+');
    cgi_decode('%20');
    cgi_decode('abc');
    try: cgi_decode('%?a');
    except: pass

sample = fuzzer()
with Coverage() as cov:
    try: cgi_decode(sample)
    except: pass

print("** covmax - cov");
print(covmax.coverage() - cov.coverage());

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
