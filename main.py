import random
import math

TOTAL_PROBLEMS = 5
MIN_THRESHOLD = 0
MAX_THRESHOLD = 10
num_correct = 0


def user_prompt():
    """
    This function returns the prompt that the user is presented with to choose
    what kind of problem they want to practice.
    """
    return """
    Enter the number of the type of arithmetic problem you want to practice.
    1) Addition
    2) Subtraction
    3) Exponential Function
    4) Pythagorean Theorem
    """


def generate_input():
    """
    This function generates a random number to act as input for an
    arithmetic problem.
    """
    return random.randint(MIN_THRESHOLD, MAX_THRESHOLD)


def create_arithmetic_problem_prompt(a, b, operator):
    """
    This function takes in two numbers and an operator and returns a string
    that is built from these three pieces of information
    """
    return "What is " + str(a) + " " + operator + " " + str(b) + "?"


def create_pythagorean_problem_prompt(a, b):
    """
    This function takes two numbers and returns the value deemed as the hypotenuse
    """
    return "What does " + (str(a)) + " squared + " + str(b) + " squared make c, the hypotenuse ?"


def create_exponential_problem_prompt(a, b):
    """
    This function takes two numbers and returns the exponential value
    """
    return "What is " + str(a) + " to the power of " + str(b) + " ?"


def assess_user_response(user_answer, true_answer):
    """
    This function takes in two answers, one of which is provided by
    the user and one of which is the correct answer. It generates an
    appropriate response depending on whether the user answers
    matches the correct answer.
    """
    if user_answer == true_answer:
        print("Correct, great work!")
        return True
    else:
        print("Incorrect. The expected answer was " + str(true_answer))
        return False


def addition(a, b):
    """
    Simple function to encapsulate addition
    """
    return a + b


def user_answer():
    """
    input by user
    """
    int(input("Your answer: "))


def true_answer():
    """
    calculated actual answer
    """


def check(operation):
    """
    checking for if user input is correct
    """
    user_answer = int(input("Your answer: "))
    true_answer = {operation}(a, b)
    correct = assess_user_response(user_answer, true_answer)
    if correct:
        num_correct += 1
    num_problems_done += 1


def subtraction(a, b):
    """
    Simple function to encapsulate subtraction
    """
    return a - b


def exponential(a, b):
    """
    Simple function to encapsulate exponential problems
    """
    return a ** b


def pythagorean(a, b):
    """
    Simple function to encapsulate the pythagorean theorem
    """
    return math.sqrt(a ** 2 + b ** 2)


def main():
    num_problems_done = 0
    num_correct = 0
    while num_problems_done < TOTAL_PROBLEMS:
        print(user_prompt())
        choice = int(input("Your choice: "))
        a = generate_input()
        b = generate_input()
        if choice == 1:
            print(create_arithmetic_problem_prompt(a, b, "+"))
            user_answer = int(input("Your answer: "))
            true_answer = addition(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        elif choice == 2:
            print(create_arithmetic_problem_prompt(a, b, "-"))
            user_answer = int(input("Your answer: "))
            true_answer = subtraction(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        elif choice == 3:
            print(create_exponential_problem_prompt(a, b))
            user_answer = int(input("Your answer: "))
            true_answer = exponential(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        elif choice == 4:
            print(create_pythagorean_problem_prompt(a, b, ))
            user_answer = int(input("Your answer: "))
            true_answer = pythagorean(a, b)
            correct = assess_user_response(user_answer, true_answer)
            if correct:
                num_correct += 1
            num_problems_done += 1
        else:
            print("Sorry, you didn't choose a valid option!")
    print("You got " + str(num_correct) + " out of 5 problems correct!")


if __name__ == "__main__":
    main()
