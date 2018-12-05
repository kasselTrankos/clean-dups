from clint.textui import puts, validators, prompt
from .pwd import red, green, blue, files
from .utils import compose
import dev.constants
from dev.db import find, updateOne
from dev.diff import dict_same, evaluate

def clean(dups):
  puts(blue('we have founded ') + red(str(len(dups))) + blue(' duplications'))
  inst_options = [{'selector':'1','prompt':'please review','return':'y'},
                  {'selector':'2','prompt':'better in other moment','return':'n'}]
  willContinue =prompt.options(green('Do you want to continue?'), inst_options)
  if willContinue == 'y': 
    generator = cleanDuplicated(dups)
    for i in dups: 
      next(generator)
    
    # next(cleanDuplicated(dups))
  else: print('quuyerioyurti')

def queryImages(image):
  query = {}
  query['name'] = image['name']
  query['$and'] = [{'path': {'$ne': image['path']}}]
  return query

def cleanDuplicated(dups):
  ignore = ['JPEGThumbnail', '_id', 'date', 'path', 'defects']

  def getToInclude(same):
    state = '1'
    for x in same:
      if x['evaluation'] != 0: 
        state = '0'
    return {
      'defects': {
        'duplicated': {
          'same': same,
          'state': state
        }
      }
    }
  for dup in dups:
    compare = dict_same(dup, ignore) 
    update = updateOne(dup) 
    print(blue('file '+dup['path']))
    diff = [compose(evaluate, compare)(img) for img in
      compose(find, queryImages)(dup)]
    updated = compose(update, getToInclude)(diff)
    print(blue('with '+str(len(diff))+' duplications '))
    then = 'GREAT'
    if updated['defects']['duplicated']['state'] == '0':
      then = 'OHHHH' 
    print(red(then))
    yield dup