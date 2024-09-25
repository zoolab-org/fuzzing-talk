#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

def cgi_decode_wrapper(s):
    if os.path.exists("cgidecode.gcda"): os.remove("cgidecode.gcda");
    result = subprocess.run(["./cgidecode", s],
                stdin = subprocess.DEVNULL,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE);
    return result.stdout;

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(cgi_decode_wrapper(sys.argv[1]))
    else:
        print("pass a string to me");

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
