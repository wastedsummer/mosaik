import json
import torchvision.datasets as dset
import torchvision.transforms as transforms



def load_json(file):
	""" Helper function to load json files and return them as dictionary. """
	try:
		with open(file) as json_file:  
		    data = json.load(json_file)
		return data
	except FileNotFoundError:
		print("\nSomething went wrong... Make sure your specified path is spelled properly and exists.\n")
	except TypeError:
		print("\nSomething went wrong... Make sure, to enter a path in form of a string.\n")




