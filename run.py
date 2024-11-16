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
    "A": "London",
    "B": "Paris",
    "C": "Moscow"
}

print(options)
print()
answer = input("Please give your answer: ")

def determine():
    if answer == "B":
        print("Correct")
    elif answer == "A":
        print("Incorrect")
    elif answer == "C":
        print("Incorrect")    
    else:
        print("not an option, please try again")

determine()


    