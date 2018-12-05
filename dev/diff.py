from dev.utils import merge


KEYNOTFOUND = '<KEYNOTFOUND>'       # KeyNotFound for dictDiff

def dict_same(origin, ignore=None):
  def compare(compared):
    same = {
      'image': compared['path']
    }
    # Check all keys in first dict
    for key in origin.keys():
      if (not key in ignore and key in compared):
        if (origin[key] ==  compared[key]):
          same[key] = origin[key]
    return same
  return compare

def evaluate(same):
  properties = ['EXIF DateTimeOriginal', 'MakerNote ImageUniqueID']
  point = 0
  for key in same:
    if (key in properties):
      point+=1
  return merge({'evaluation': point}, same)
