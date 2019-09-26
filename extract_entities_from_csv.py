import csv
from urllib.request import urlopen
import codecs

def __fetch_csv_file(url):
  response = urlopen(url)
  cr = csv.reader(codecs.iterdecode(response, 'utf-8'))
  return cr

def extract_entities_from_csv(url):
  print("Extracting data from %s" % url)
  cr = __fetch_csv_file(url)
  entities =  {}
  for index, row in enumerate(cr):
    if index == 0:
      try:
        if row[0] != "id" or row[1] != "imageUrl":
          raise Exception
      except:
        raise Exception("Incorrect data inside csv file")
      continue
    
    try:
      identifier = row[0]
      imageUrl = row[1]
    except:
      print("Problem in the line %s of the csv file", index)
    
    if entities.get(identifier) is None:
      entities[identifier] = []
    
    entities[identifier].append(imageUrl)
  return entities
    
    
