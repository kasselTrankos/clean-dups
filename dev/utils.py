import functools
import os
import sys
import numpy as np
from time import sleep
from clint.textui import colored

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
  # print(colored.blue('ADD '))
  def put(image):
    sys.stdout.write('\033[K duplicated ' + colored.red(image)+ '\r')
    # print(colored.red('found duplicate '+ image), end = '\r')
    # sleep(0.001)
    return image
  names = [getName(x) for x in items ]
  return [put(x) for x in items if names.count(getName(x)) > 1 ]