#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
from dev.pwd import red, green, blue, images, duplicatedByName
from dev.utils import compose
from dev.cleaner import clean
from clint.textui import puts
from pprint import pprint
import dev.constants

dev.constants.init()
puts(blue('For find images duplicated, first set your folder:'))
dev.constants.data['folder'] = input() or '/media'
# value = folder(dev.constants.data['folder'])

imgs = images(dev.constants.data['folder'])
dups = duplicatedByName(imgs)
## made to mongodb
if len(dups) > 0:
  clean(dups)
else:
  puts(green('no duplicated images'))
