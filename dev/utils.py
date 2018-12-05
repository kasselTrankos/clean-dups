import functools
import os
import numpy as np

def compose(*functions):
  return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def getName(file):
  baseName = os.path.basename(file)
  return os.path.splitext(baseName)[0]

def getCount (items):
  return len(items)

def merge(*argv):
  dict = {}
  for arg in argv:
    dict.update(arg)
  return dict

def getDuplicated(items):
  names = [getName(x) for x in items ]
  return [x for x in items if names.count(getName(x)) > 1 ]