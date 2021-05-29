import json

data = json.load(open("package.json"))

def translate(word):
    if word in data:
        return data(word)
    else:
        return "The words not there, double check your spelling"

word = input("enter word: ")

print(translate(word))
