import random
def Answer(answer_number):
    if answer_number == 1:
        return "You will win the lottery today!"
    elif answer_number == 2:
        return "you will probably cry tonight...alone..."
    elif answer_number == 3:
        return "Somebody loves you!"
    elif answer_number == 4:
        return "Nobody loves you"
    elif answer_number == 5:
        return "Go away, ask again later"
    elif answer_number == 6:
        return "No.. just.. no.."
    elif answer_number == 7:
        return "Do you really believe this crap?"
    elif answer_number == 8:
        return "I'm going to say Yes."
    elif answer_number == 9:
        return "I am unsure.. lets just say no..."

r= random.randint(1,9)
fortune = Answer(r)
print(fortune)
