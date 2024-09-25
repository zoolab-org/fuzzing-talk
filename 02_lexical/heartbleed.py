#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..');
from fuzzer import *

secrets = ("<space for reply>" + fuzzer(100) +
           "<secret-certificate>" + fuzzer(100) +
           "<secret-key>" + fuzzer(100) + "<other-secrets>")

def heartbeat(reply, length, memory):
    memory = reply + memory[len(reply):]
    return memory[:length];

print(heartbeat("potato", 6, secrets));
print(heartbeat("bird",   4, secrets));
print(heartbeat("hat",  500, secrets));

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
