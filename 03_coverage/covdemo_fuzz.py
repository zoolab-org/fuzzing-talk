#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')
from fuzzer import *
from cgidecode import *

# one round
trials = 10000
if len(sys.argv) > 1: trials = int(sys.argv[1])
for _ in range(trials):
    s = fuzzer()
    try: cgi_decode(s)
    except ValueError: pass
    except Exception as ex:
        print("***", s)
        print(repr(ex))
        

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
