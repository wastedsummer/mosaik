from _conf import DATA_PATH
from utils import load_json


import torchvision.datasets as dset
import torchvision.transforms as transforms



# print(type(DATA_PATH))
test_annotations = load_json(DATA_PATH + 'train2019.json')

# print(test_annotations['annotations'][0])
# print(test_annotations['categories'][1000])



