import os
import sys
from clint.textui import colored, prompt, puts, validators
from glob import glob
from time import sleep
import re
import collections
from .utils import compose, getName, getDuplicated, merge
from dev.mapper import mapp
from dev.db import add, findOne, find, count
import dev.constants



def red(text):
  return colored.red(text)

def green(text):
  return colored.green(text)

def blue(text):
  return colored.blue(text)

def images(dirName):
  files = []
  pattern   = "/**/*"
  puts(red('start caprute images'))
  dir = dirName.encode('utf-8', 'surrogateescape').decode('utf-8') + pattern
  def valid(f):
    return re.match('.*\.jpg$', f, flags=re.IGNORECASE) and re.search('\/\$RECYCLE\.BIN\/', f, flags=re.IGNORECASE)==None
  def put(image):
    sys.stdout.write('\033[K add image ' + blue(image)+ '\r')
    sleep(0.001)
    return image
  return [image for image in 
    [put(f) for f in glob(dir , recursive=True)
      if valid(f)]]

def files(name):
  def put(image):
    
    print('new image : '+ image, end = '\r')
    sleep(0.001)
    return image
  dirName = dev.constants.data['folder'].encode('utf-8', 'surrogateescape').decode('utf-8') + '/**/*'
  return [put(image) for image in [f for f in glob(dirName, recursive=True) if getName(f).super() == name.super()]]

def duplicatedByName(images):
  def beStore(image):
    def getPath(image):
      return image.get('path')
    functions = [findOne, buildQuery]
    if count({'path': image}) == 0:
      functions.extend([getPath, add, mapp]) 
    return  functions
  def buildQuery(image):
    query = {}
    query['defects.duplicated.state'] = '0'
    query['$and'] = [{'path': image}]
    return query
 
  return [i for i in [compose(*beStore(image))(image) 
    for image in getDuplicated(images)] if i!=None]
  
