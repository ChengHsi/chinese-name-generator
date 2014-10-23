#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
Random Chinese Name Generator
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = ' Cheng-Hsi (curiojustus@gmail.com)'
__copyright__ = 'Copyright (c) 2014 Cheng-Hsi'
__license__ = 'New-style BSD'
__vcs_id__ = '$Id$'
__version__ = '0.1.0'

from random import choice, sample, randint
import sys
import argparse
import os
import name as name


def rand_chi_name(n):
    forename_list = name.forename.split(' ')
    first_name_list = name.first_name.split(' ')
    for i in range(0, n):
        yield choice(forename_list) + ''.join([x for x in sample(first_name_list, randint(1, 2))])


def clean_strings(string):
    while '  ' in string:
        string = string.replace('\xe3\x80\x80', '').replace('\n', '').replace('  ', ' ')
    return string


def write_clean_strings():
    import ast
    import codegen
    try:
        with open('name.py', 'rw') as file1:
            p = ast.parse(file1)
            print(codegen.to_source(p))
    except SyntaxError as e:
        print e


def string2list(string):
    clean_string = clean_strings(string)
    namelist = clean_string.split(' ')
    return namelist


if __name__ == '__main__':
    oparser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]), add_help=True)
    oparser.add_argument('count', metavar='Count', type=int, nargs='?', help='The count of names to be generated, default to 1')
    oparser.add_argument('--boy', dest='is_male', action='store_true', help='Generate only male names')
    oparser.add_argument('--girl', dest='is_male', action='store_false', help='Generate only female names')
    oparser.set_defaults(is_male=None, count=1)
    args = oparser.parse_args()
    print args
    # print(args.accumulate(args.integers))
    for item in rand_chi_name(args.count):
        print item
    # print clean_strings(name.hundred)
    # print string2list(name.tw_hundred)[42]
    # print len(string2list(name.thousand))
    # write_clean_strings()
