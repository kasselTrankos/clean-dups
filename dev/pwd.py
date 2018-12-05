import os
from clint.textui import colored, prompt, puts, validators
from glob import glob
import re
import collections
from .utils import compose, getName, getDuplicated, merge
from dev.mapper import mapp
from dev.db import add, findOne, count
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
  for image in [f for f in glob(dirName.encode('utf-8', 'surrogateescape').decode('utf-8') + pattern, recursive=True) if re.match('.*\.jpg$', f, flags=re.IGNORECASE)]:
    files.append(image)

  return files

def files(name):
  dirName = dev.constants.data['folder'].encode('utf-8', 'surrogateescape').decode('utf-8') + '/**/*'
  return [image for image in [f for f in glob(dirName, recursive=True) if getName(f).super() == name.super()]]

def duplicatedByName(images):
  def beStore(image):
    def getPath(image):
      return image.get('path')
    functions = [findOne, buildQuery]
    if count({'path': image}) == 0:
      functions.extend([getPath, add, mapp]) 
    return  functions
  def buildQuery(image):
    return merge(
      {'defects': {'duplicated': {'state': '0'}}},
      {'path': image})
      
  return [i for i in [compose(*beStore(image))(image) 
    for image in getDuplicated(images)] if i!=None]
  
