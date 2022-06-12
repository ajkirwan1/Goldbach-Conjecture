import SerialPrime as sp
import Error
import timer
import UserInput
t = timer.Timer()


if __name__ == '__main__':

    chosen_number = UserInput.user_input()
    list_of_all_numbers = sp.produce_number_list(chosen_number)
    one_pair_of_primes = sp.single_pair(list_of_all_numbers, chosen_number)

    if type(one_pair_of_primes) is list:
        print(f"A pair of prime numbers that sum to {chosen_number} is {one_pair_of_primes}")
        if chosen_number > 100000:
            print(f"Calculating all primes-pairs for the number {chosen_number} will be computationally expensive and may crash")
            print("your system. We cannot allow this!")
        else:

            calculate_all_primes = UserInput.program_mode()
            print(calculate_all_primes)
        if chosen_number <= 100000:
            if calculate_all_primes == "Yes":
                All_numbers = sp.produce_number_list(chosen_number)
                All_pairs = sp.all_pairs(All_numbers, chosen_number)
                List_of_all_primes = sp.remove_non_primes(All_pairs, All_numbers)
                print(List_of_all_primes)
            else:
                print("You have selected no and so the program will now end")
        else:
            pass

