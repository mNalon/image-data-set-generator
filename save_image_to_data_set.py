from urllib.parse import urlparse
import os
import requests
import uuid

from config import __TEMP_PATH

def __create_directory_if_not_exists(directory):
  if not os.path.exists(directory):
    os.makedirs(directory)

def __get_file_extension(url):
  path = urlparse(url).path
  ext = os.path.splitext(path)[1]
  return ext

def save_image_to_data_set(identifier, image_url):
  target_directory = "%s/%s" % (__TEMP_PATH, identifier)
  __create_directory_if_not_exists(target_directory)
  img_data = requests.get(image_url).content
  file_name = uuid.uuid4()
  file_ext = __get_file_extension(image_url)
  file_uri = "%s/%s%s" % (target_directory, file_name, file_ext)
  print("saving image %s at %s" % (image_url, file_uri))
  with open(file_uri, 'wb') as handler:
      handler.write(img_data)
