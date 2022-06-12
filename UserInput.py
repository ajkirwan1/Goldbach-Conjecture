
import Error
import time

# The UserInput.py script contains a single function: user_input(). This function takes no arguments and is run in
# main.py. It designed to request  a positive even integer that's greater than 2, and returns this value.
# The bulk of the function is wrapped in a while loop, and contains Try and Except to handle errors resulting from
# a number of non-valid user input values such as odd numbers, numbers less than 2, and non-integer values. It also
# prevents the user from entering a viable number larger than 100000, which may result in long processing times.


def program_mode():
    print("You now have the option to calculate all prime-pairs. Would you like to do this?")
    print("Type Yes or No:")
    while True:
        try:
            x = input().capitalize()
            if x == 'Yes':
                print("You chose yes")
            elif x == "No":
                print("You chose no")
            else:
                raise Error.NotYesOrNoError

        except Error.NotYesOrNoError:
            print("The number you chose does not fit the criteria")
            print("Would you like to try again? Type Yes or No:")
            answer = input().capitalize()
            if answer == "No":
                break
            elif answer == "Yes":
                print("You'll now make another attempt")
            else:
                print(f"You typed \'{answer}\' which is not a viable input")
                print("The program will now end")
                break
        else:
            return x


def user_input():
    print("Goldbach's conjecture states that every even natural number greater than 2 is the sum of two prime numbers.")
    print("More details can be found here: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture")
    print("This program will find two primes for a number of choice, providing it fits the above criteria.")
    print("Later, you will be given the option to find all prime numbers that sum to your choice. However, be aware")
    print("that this calculation may take a significant amount of time, particularly if you chose a larger number.")
    while True:
        print("Please enter a positive even number greater than 2:\n")
        try:
            x = int(input())
            if x <= 2:
                raise Error.NotGreaterThan2Error
            if x % 2 != 0:
                raise Error.OddNumberError
            if x > 100000000:
                raise Error.LargeNumberError
        except ValueError:
            print("The number you chose does not fit criteria")
            print("Would you like to try again? Type Yes or No:")
            answer = input().capitalize()
            if answer == "No":
                break
            elif answer == "Yes":
                print("You'll now make another attempt")
            else:
                print(f"You typed \'{answer}\' which is not a viable input")
                print("The program will now end")
                break
        except Error.OddNumberError:
            print("The number you chose is odd. The input number must be even")
            print("Would you like to try again? Type Yes or No:")
            answer = input().capitalize()
            print(f"You answered {answer}")
            if answer == "No":
                break
            elif answer == "Yes":
                print("You'll now make another attempt")
            else:
                print(f"You typed \'{answer}\' which is not a viable input")
                print("The program will now end")
                break
        except Error.NotGreaterThan2Error:
            print("The number you chose is not greater than 2")
            print("Would you like to try again? Type Yes or No")
            answer = input().capitalize()
            if answer == "No":
                break
            elif answer == "Yes":
                print("You'll now make another attempt")
            else:
                print(f"You typed \'{answer}\' which is not a viable input")
                print("The program will now end")
                break
        except Error.LargeNumberError:
            print("The number you chose is too large and will likely crash the system")
            print("Would you like to try again? Type Yes or No")
            answer = input().capitalize()
            if answer == "No":
                break
            elif answer == "Yes":
                print("You'll now make another attempt")
            else:
                print(f"You typed \'{answer}\' which is not a viable input")
                print("The program will now end")
                break
        except Exception as e:
            print(f"There is another error: {e}")
        else:
            print("You have chosen a viable number")
            return x
