import json
import pprint
import difflib
from difflib import get_close_matches

# how to load a json data in python 
data = json.load(open("C:\\Users\\demmy\\Downloads\\Python\\Dictionary\\data.json", encoding='utf-8'))
# print(data)
print(data['Paris'])