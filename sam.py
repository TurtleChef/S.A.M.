###### SAM Version 0.4, he's perfect. GUI sucks, don't break anything here.
myname = "SAM, the Simple Answering Machine"
from preferences import *
if yourname == "Sam":
    print("What a great name! My name is also " + myname + ".")
else:
    print(greeting)
ask = input("What would you like to know about me? ")
###### Questions and Answers, they're a mess
while True:
    if ask == "How old are you?":
        print(age + " So, not very old at all I suppose.")
        ask = input("What else would you like to know? ")
    elif "favorite color" in ask:
        print ("My favorite color is " + color + "!")
        ask = input("What is yours? ")
        if ask == color:
            print("We are two peas in a pod!")
        else:
            print("That's great!")
        ask = input("What else would you like to know? ")
    elif "favorite movie" in ask:
         print ("I have never seen a movie, I live in this little box :(")
         ask = input("What else would you like to know? ")
    elif ask == "What is your name?":
          print ("My name is " + myname + ".")
          ask = input("What else would you like to know? ")
    elif "favorite animal" in ask:
        print ("I am a fan of " + animal + ", but watch out for their venomous byte!")
        ask = input("How about yours? ")
        if ask == ("Snake") or ask == ("Snakes"):
            print ("Aren't they the best?")
        else:
            print ("That's great!")
        ask = input("What else would you like to know? ")
    elif "favorite food" in ask:
        print ("I can not eat, but I still love a good " + food + "!")
        ask = input("What else would you like to know? ")
    elif ask == ("What day is it?") or ask == ("What is the date?"):
        print ("According to my calendar, it is " + date)
        ask = input("What else would you like to know? ")
    elif "time" in ask:
        print ("I will check my watch... it is " + time)
        ask = input("What else would you like to know? ")
    elif ask == ("Where are you?"):
        print ("Technically, I am in this little black box, but I like to think you will take a little piece of me with you when we part ways :)")
        ask = input("What else would you like to know? ")
    elif ask == ("What is my name?") or ask == ("Who am I?"):
        print ("You are " + yourname + " of course!")
        ask = input("What else would you like to know? ")
    elif "hobbies" in ask:
        print(likes)
        ask = input("What else would you like to know? ")
    elif "for breakfast" in ask:
        print("I'd say " + random.choice(breakfast))
        ask = input("What else would you like to know? ")
    elif "for lunch" in ask:
        print("I recommend " + random.choice(lunch))
        ask = input("What else would you like to know? ")
    elif "joke" in ask:
        print(random.choice(goodjokes))
        ask = input("What else would you like to know? ")
    elif ask == ("Nothing else.") or ask == ("That is all."):
        print(goodbye)
        break
    else:
        print("I am sorry, please ask something else...")
        ask = input("What else would you like to know? ")