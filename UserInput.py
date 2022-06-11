
import Error


def user_input():
    while True:
        print("Please enter a positive even number greater than 2:\n")
        try:
            x = int(input())
            if x <= 2:
                raise Error.NotGreaterThan2Error
            if x % 2 != 0:
                raise Error.OddNumberError
            if x >= 100000:
                raise Error.LargeNumberError
            #break
        except ValueError:
            print("The number you chose does not fit criteria")
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
        except Error.OddNumberError:
            print("The number you chose is odd. The input number must be even")
            print("Would you like to try again? Type Yes or No")
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
