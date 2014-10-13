#pirate_bar.py

import random

questionsDict = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
}

ingredientsDict = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def ask_customer(questionsDict):
    """Asks customer what drinks they like"""
    #Generate Data structure:
    answerDict = {}
    for question in questionsDict.keys():
        answerDict[question] = None
    #Populate Data structure:
    for question in questionsDict.keys():
        answer = raw_input(questionsDict[question])
        if answer.lower() == 'yes' or answer.lower() == 'y':
            answerDict[question] = True
        else:
            answerDict[question] = False
    return answerDict

def construct_drink(answerDict):
    """Construct drink for customer given their likes."""
    output_drink = []
    for preference in answerDict.keys():
        if answerDict[preference] == True:
            output_drink.append(random.choice(ingredientsDict[preference]))
    return output_drink


def main():
    answerDict = ask_customer(questionsDict)
    output_drink = construct_drink(answerDict)
    print "I've added the following to yer drink"
    for element in output_drink:
        print element
    print "Hope ye enjoy it me hearty!"

if __name__ == '__main__':
    main()

