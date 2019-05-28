# Import the modules
import sys
import random

ans = True
def answer(i):
    switcher={
        1:"Yes, my friend",
        2:'No, my friend',
        3:'Did I mention I hate you. My friend',
        4:'Screens please!',
        5:'What are you doing, my friend?',
        6:'Look at me! My friend, look at me!',
        7:"Sorreh!",
        8:'Luvleh!'
        }
    return switcher.get(i,'Invalid')

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    if question =="":
        sys.exit()
    
    answers = random.randint(1,8)
    display = answer(answers)
    print("\nI reply {0}".format(display))