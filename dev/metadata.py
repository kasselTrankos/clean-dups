import exifread

def getMetadata(image):
  _file = open(image, 'rb')
  tags =  exifread.process_file(_file)
  return  {i: str(tags[i]) for i in tags.keys()}