import json
from difflib import get_close_matches
#load data
data = json.load(open("DicData.json"))

def translate(word):
    #Convert all letter in to lower case
    word = word.lower()
    #Check all lower case words in data
    if word in data:
        return data[word]
    #Convert word into tital(like- Tital) and then check in data
    elif word.title() in data:
        return data[word.title()]
    #Convert word into uppercase and then check in data
    elif word.upper() in data:
        return data[word.upper()] 
    #This elif are check the closest match word into data keys 
    elif len(get_close_matches(word,data.keys())) > 0:
            print("Did u mean %s insted" %get_close_matches(word,data.keys())[0])
            decied = input("Press y for Yes / n for No :- ")
            if decied =='y':
                return data[get_close_matches(word,data.keys())[0]]
            elif decied =='n':
                print("You entered somthing mistake word plzzz chech it again........")
            else:
                print("Worng input")

    else:
        print("You entered worng word plzzz check it again!!!!")
#Take user input (user inputput word that he/she want to search)
word = input("what do u want to search :- ")
#Function call ans save in output variable
output = translate(word)
#Output formatting 
if type(output) == list:
    for itam in output:
        print(itam)
else:
    print(output)
