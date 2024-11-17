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

class Countries:
    """Lists the countries"""
    def __init__(self, country, capital, incorrect_1, incorrect_2, a, b, c):
        self.country = country
        self.capital = capital
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2 
        self.a = a
        self.b = b
        self.c = c
    
    def question(self):
        """the question"""
        return f"What is the capital of {self.country}?\nIs it {self.a}: {self.incorrect_1}, {self.b}: {self.incorrect_2} or {self.c}: {self.capital}"

question_1 = Countries("United States", "New York", "Los Angeles", "Washington DC", "A", "B", "C")
print()
print(question_1.question())
question_2 = Countries("China", "Beijing", "Hong Kong", "Shanghai", "A", "B", "C")
print()
print(question_2.question())
question_3 = Countries("Germany", "Berlin", "Hamburg", "Munich", "A", "B", "C")
print()
print(question_3.question())

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
        the_question()
        print()
        the_options()
        print()
determine_if_c_is_the_corrrect_answer()








    