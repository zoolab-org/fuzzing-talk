#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import random

def my_sqrt(x):
    """Computes the square root of x, using the Newton-Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

def my_sqrt_with_log(x):
    """Computes the square root of x, using the Newton–Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        print("approx =", approx)  # <-- New
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

def assertEquals(x, y, epsilon=1e-8): assert abs(x - y) < epsilon

def my_sqrt_checked(x):
    root = my_sqrt(x)
    assertEquals(root * root, x)
    return root

def testcases():
    t = time.time();
    for i in range(1, 10000):
        assertEquals(my_sqrt(i) * my_sqrt(i), i);
    print(time.time() - t);

def testcases_random():
    t = time.time();
    for i in range(1, 10000):
        x = 1 + random.random() * 1000000
        assertEquals(my_sqrt(x) * my_sqrt(x), x);
    print(time.time() - t);

# run as a standalong program
if __name__ == '__main__':
    try:
        x = float(sys.argv[1]);
    except IndexError: print("Insufficient Arguments");
    except ValueError: print("Illegal Input", sys.argv[1]);
    else:
        if x <= 0: print("Illegal Number", sys.argv[1]);
        else: print('The root of', x, 'is', my_sqrt_checked(x))

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
