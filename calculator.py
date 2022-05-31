# simple CLI calculator in python stage 1 task @Zuri2022 internship

print(""" Select arithmetic operation: 
            1.for Addition
            2.for Division
            3.for Modulus
            4.for Multiplication
            5. for Subtraction
""")
# print answer function
def print_answer(one, two, operation, answer):
    print(one, operation, two, "=", answer)
def addition(number1, number2):
    return number1 + number2

while True:
    selection = int(input("please select options 1 to 5 to perform your arithmetic operation: "))
    if selection in (1, 2, 3, 4, 5):
        first_number = int(input("please enter the first number: "))
        second_number = int(input("please enter the second number: "))

        if selection == 1:
            # perform addition operation
            answer = addition(first_number, second_number)
            print_answer(first_number, second_number, "+", answer)
        elif selection == 2:
            # perform division operation
            answer = first_number / second_number
            print_answer(first_number, second_number, "/", answer)
        elif selection == 3:
            # perform modulus operation
            answer = first_number % second_number
            print_answer(first_number, second_number, "%", answer)
        elif selection == 4:
            # perform multiplication operation
            answer = first_number * second_number
            print_answer(first_number, second_number, "*", answer)
        elif selection == 5:
            # perform subtraction operation
            answer = first_number - second_number
            print_answer(first_number, second_number, "-", answer)

            # ask the user if they want to continue with another operation
            continue_operation = input("Do you want to continue with another operation? (1. Yes/2.No): ")
            if continue_operation == "1":
                continue
            elif continue_operation == "2":
                print("Thank you for using CLI-Python-Calculator by @ViashimaCollins")
                break
    else:
        print("Invalid selection. Please selection option from 1 to 5.")
        continue
# end of program
# viashimaCollins
# github.com/clins10
#twitter.com/ViashimaCollins
#linkedin.com/in/collinsv

             
        



