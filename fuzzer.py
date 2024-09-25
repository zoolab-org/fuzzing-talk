#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import tempfile
import random
import subprocess

def fuzzer(max_length=100, char_start=32, char_range=32):
    """A string of up to `max_length` characters
       in the range [`char_start`, `char_start` + `char_range`]"""
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

def get_tempfile(basename = "input.txt"):
    tempdir = tempfile.mkdtemp();
    return os.path.join(tempdir, basename), tempdir

def run(cmdarg, stdin = subprocess.DEVNULL, stdout = subprocess.PIPE, stderr = subprocess.PIPE):
    return subprocess.run(cmdarg, # [program, FILE],
                stdin = stdin, stdout = stdout, stderr = stderr,
                universal_newlines = True)
#   print("stdout:", result.stdout)
#   print("stderr:", result.stderr)
#   print("return code:", result.returncode)

_trace = None;

def tracer(frame, event, arg = None):
    global _trace;
    # available events: call, return, line, exception
    if event != 'line': return tracer
    #
    funcname = frame.f_code.co_name
    lineno = frame.f_lineno
    if _trace != None:
        _trace.append((funcname, lineno));
    else:
        print("event '{}': {} @ {}".format(event, funcname, lineno));
    return tracer

def coverage_enable(output = None, tracer = tracer):
    global _trace;
    old = sys.gettrace();
    _trace = output;
    sys.settrace(tracer);
    return old

def coverage_disable(old = None):
    global _trace;
    sys.settrace(old);
    _trace = None;

class Coverage:
    # Trace function
    def traceit(self, frame, event, arg):
        if self.original_trace_function is not None:
            self.original_trace_function(frame, event, arg)

        if event == "line":
            function_name = frame.f_code.co_name
            lineno = frame.f_lineno
            self._trace.append((function_name, lineno))

        return self.traceit

    def __init__(self):
        self._trace = []
        self.original_trace_function = None

    # Start of `with` block
    def __enter__(self):
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)
        return self

    # End of `with` block
    def __exit__(self, exc_type, exc_value, tb):
        sys.settrace(self.original_trace_function)

    def trace(self):
        """The list of executed lines, as (function_name, line_number) pairs"""
        return self._trace

    def coverage(self):
        """The set of executed lines, as (function_name, line_number) pairs"""
        return set(self.trace())

def population_coverage(seeds, function):
    cumulative_coverage = []
    all_coverage = set()

    for s in seeds:
        with Coverage() as cov:
            try: function(s)
            except: pass
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))

    return all_coverage, cumulative_coverage

def run_gcov(c_file):
    result = subprocess.run([ "gcov", c_file],
                stdin = subprocess.DEVNULL,
                stdout = subprocess.DEVNULL,
                stderr = subprocess.DEVNULL)

def read_gcov_coverage(c_file):
    gcov_file = c_file + ".gcov"
    coverage = set()
    with open(gcov_file) as file:
        for line in file.readlines():
            elems = line.split(':')
            covered = elems[0].strip()
            line_number = int(elems[1].strip())
#           if covered.startswith('-') or covered.startswith('#'): continue
            if covered[0] == '-' or covered[0] == '#': continue
            coverage.add((c_file, line_number))
    return coverage

def gcov_coverage(c_file):
    run_gcov(c_file)
    return read_gcov_coverage(c_file)

### mutational fuzzing

def delete_random_character(s):
    if s == "": return s
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1:]

def insert_random_character(s):
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]

def flip_random_character(s):
    if s == "": return s
    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    return s[:pos] + chr(ord(c) ^ bit) + s[pos + 1:]

def mutate(s):
    mutators = [
        delete_random_character,
        insert_random_character,
        flip_random_character
    ]
    mutator = random.choice(mutators)
    return mutator(s)

# vim: set tabstop=4 expandtab shiftwidth=4 softtabstop=4 number cindent fileencoding=utf-8 :
