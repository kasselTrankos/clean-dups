from datetime import datetime
from .metadata import getMetadata
import unicodedata
from .utils import merge, getName, getDuplicated, getCount


def buildImageObject(image):
  date = datetime.now()
  return {
    'name': getName(image),
    'path': image,
    'date':{
      'value': date,
      'spain':  datetime.strftime(date , '%d/%m/%Y')
    }
  }

def mapp(image):
  return merge(
    buildImageObject(image), {
      'defects': {
        'duplicated': {
          'state': '0'
        }
      }
    }, 
    getMetadata(image))