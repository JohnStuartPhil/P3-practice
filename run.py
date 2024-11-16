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
question = "What is the Capital of {country}?"
print(question)
print()

options = {
    "A": "Nice",
    "B": "Paris",
    "C": "Lyon"
}

print(options)
print()
answer = input("Please select an option, A, B or C: ")

def determine():
    if answer.upper() == "B":
        print("Correct")
    elif answer.upper() == "A":
        print("Incorrect")
    elif answer.upper() == "C":
        print("Incorrect")    
    else:
        print("This is not an option, please try again")

determine()


    