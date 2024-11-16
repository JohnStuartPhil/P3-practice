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
    """
    Puts forward the question
    """
    question = "What is the Capital of the United States?"
    print(question)
the_question()

print()

def the_options():
    """
    Lists the options
    """
    options = {
        "The options are:"
        " "
        "A": "Los Angeles",
        "B": "New York",
        "C": "Washington DC"
        }
    print(options)
the_options()

print()

def determine_if_c_is_the_corrrect_answer():
    """
    determines the output once the user has input A/a, B/b, C/c or something else
    """
    answer = input("Please select an option of A, B or C: ")
    print()
    print(f"You selected {answer}")
    print()

    if answer.upper() == "C":
        print(f"Well done, {answer} is the correct answer")
        print()
    elif answer.upper() == "A":
        print(f"{answer} is not the correct answer")
        print()
    elif answer.upper() == "B":
        print(f"{answer} is not the correct answer")    
        print()
    else:
        print(f"{answer} is not an option, please try again and choose an option of A, B or C")
        print()
determine_if_c_is_the_corrrect_answer()








    