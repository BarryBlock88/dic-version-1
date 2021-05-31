import json

#load JSON data
data = json.load(open("diction.json"))

#take word from user
word = input('Enter a word SVP: ')

#function to return meaning of the word from data
def getMeaning(w):
    #for case sensitivity
    w = w.lower()
    #if-else to check word exist in our data or not
    if w in data:
        return data[w]
    #give matching word
    elif w not in data:
        print("Did you mean ... instead? Enter Y if yes or N if no: ")
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data
        elif choice == 'n':
            return "Hmm Nope sorry, Please double check your spelling."
        else:
            return "Huh, We didn't understand your entry."
    else:
        return "It can be hard, but that word doesn't exist. Please try again."

#function call to get meaning of the word entered by user
meaning = getMeaning(word)

#printing meaning of the word in console
if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)