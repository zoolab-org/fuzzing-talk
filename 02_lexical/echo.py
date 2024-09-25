#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

sys.path.append('..');
from fuzzer import *

run(["/bin/echo", "rm", "-rf", fuzzer()], stdout = None);


# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
