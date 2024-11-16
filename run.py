#question = input("What is the capital of France? ")
#print()
#capital = "Paris"
#answer = "The capital of France is " + capital
#print(answer)

#question = input("What is the capital of France? ")
#print(f"You answered: {question}")
#answer = 'Paris'
#print()
#print(f"The correct answer is: {answer}")

#question = input("What is the capital of France? ")
#print(question)
#answer = "Paris"
#collective = ("It is " + answer)
#print(collective)

#From String Methods
#my_string = "HELLO WORLD"
#greetings = my_string.replace("WORLD", "Dave")
#print(greetings)


print()

def the_question():
    question = "What is the Capital of the United States?"
    print(question)

the_question()

print()

def the_options():
    options = {
        "A": "Los Angeles",
        "B": "New York",
        "C": "Washington DC"
        }
    print(options)

the_options()

print()

answer = input("Please select an option, A, B or C:\n")
print(answer)


def determine():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    if answer.upper() == "C":
        print("Correct answer")
    elif answer.upper() == "A":
        print("Incorrect answer")
    elif answer.upper() == "B":
        print("Incorrect answer")    
    else:
        print("This is not an option, please try again")
        the_question()
        the_options()
determine()








    