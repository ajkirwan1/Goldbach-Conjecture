
import Error


def user_input():
    while True:
        print("Please enter a positive even number (integer) greater than 2:\n")
        try:
            x = int(input())
            if x == 0:
                raise Error.ZeroError
            if x == 1 or x == 2:
                raise Error.TwoOrOneError
            if x % 2 != 0:
                raise Error.OddNumberError
            if x >= 1000000000:
                raise Error.LargeNumberError
            if x >= 1000000:
                print("This number is large. Would you like to run in parallel to save time?")
            #break
        except ValueError:
            print("Value error")
            print("Would you like to try again? Type Y or N")
            answer = input().capitalize()
            if answer == "No":
                break
            elif answer == "Yes":
                print("You'll now make another attempt")
            else:
                print(f"You typed \'{answer}\' which is not a viable input")
                print("The program will now end")
                break
        except Error.ZeroError:
            print("Zero is not defined")
            print("Would you like to try again? Type \'Yes\' or \'No\'")
            answer = (input()).capitalize()
            if answer == "No":
                break
            elif answer == "Yes":
                print("You'll now make another attempt")
            else:
                print(f"You typed \'{answer}\' which is not a viable input")
                print("The program will now end")
                break
        except Error.TwoOrOneError:
            print("Number needs to be more than 2")
            print("Would you like to try again? Type \'Yes\' or \'No\'")
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
            print("Would you like to try again? Type \'Yes\' or \'No\'")
            answer = input()
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
            print("Would you like to try again? Type \'Yes\' or \'No\'")
            answer = input()
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
            print("You have successfully chosen a viable number")
            return x
