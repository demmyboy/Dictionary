import json
import pprint
import difflib
from difflib import get_close_matches

# how to load a json data in python 
data = json.load(open("C:\\Users\\demmy\\Downloads\\Python\\Dictionary\\data.json", encoding='utf-8'))
# print(data)
# print(data['Paris'])

# function that gets the name from the dictionary json, changes the word to lower
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        question = input("Did you mean '%s' instead? if YES, type Y, if NO, type N: " % get_close_matches(word, data.keys())[0])
        question = question.upper() 
        if question == "Y": 
            return data[get_close_matches(word, data.keys())[0]] 
        elif question == "N": 
            return "Word doesnt exist, please check again."
        else:
            return "You need to type Y or N."  
    else: 
        return "Word can not be found. Think better."

searchWord = input('ENTER A WORD TO SEARCH: ')

output = translate(searchWord)

if type(output) == list: 
    for item in output: 
        print("Meaning --- " + item)
else: 
    print(output)

   
# print(translate(searchWord))



