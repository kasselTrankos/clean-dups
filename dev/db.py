from pymongo import MongoClient
from .utils import compose

db='mongodb://localhost:27017/'
def conn():
  return MongoClient(db).images

def add(image):
  bbdd = conn()
  image['_id'] = bbdd.duplicates.insert_one(image).inserted_id
  return image

def adds(images):
  return [add(image) for image in images if count(image) == 0]

def count(query):
  bbdd = conn()
  return bbdd.duplicates.count(query)
  
def findOne(query):
  bbdd = conn()
  return bbdd.duplicates.find_one(query)

def find(query):
  bbdd = conn()
  return list(bbdd.duplicates.find(query))

def updateOne(image):
  bbdd = conn()
  def update(inc):
    bbdd.duplicates.update_one({'_id': image['_id']}, {'$set':inc}, upsert=False)
    return inc
  return update 

