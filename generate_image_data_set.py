from config import TITLES_DATA_SET_CSV_URL, __TEMP_PATH

import shutil

from extract_entities_from_csv import extract_entities_from_csv
from save_image_to_data_set import save_image_to_data_set

print("initializing the images dataset creation")

print ("erasing all data on %s" % (__TEMP_PATH))
try:
  shutil.rmtree(__TEMP_PATH)
except Exception as e:
  print('it was not possible erase the temp_path')
  print(e)

entities = extract_entities_from_csv(TITLES_DATA_SET_CSV_URL)

for identifier, imagesUrls in entities.items():
  for image_url in imagesUrls:
    save_image_to_data_set(identifier, image_url)

print ("ending the images dataset creation")