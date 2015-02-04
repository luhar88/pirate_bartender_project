import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def get_customer_choice():
    '''Get customers choice for drink'''
    try:
        print "Please reply with a True/False"
        choice = {}
        for option in questions:         
            answer = raw_input(questions[option] + " ")        
            if answer == "true":            
                choice[option] = True
            else:
                choice[option] = False
    except Exception, e:
        raise e
    else:
        return choice

def create_drink(choice):
    '''Create a drink'''    
    try:
        drink = []
        for ingredient in choice:
            if choice[ingredient]:
                drink.append(random.choice(ingredients[ingredient]))        
    except Exception, e:
        raise e
    else:
        print drink

def main():
    customer_interested = "yes"
    while not customer_interested == "no":        
        customer_interested = raw_input("Would you like a drink? \n reply with yes or no\n")
        if customer_interested == "no":
            break
        choice = get_customer_choice()
        create_drink(choice)

if __name__ == '__main__':
    main()
