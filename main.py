import SerialPrime as Sp
import Error
import timer
import UserInput
t = timer.Timer()


if __name__ == '__main__':

    chosen_number = UserInput.user_input()
    print(f"You chose the number {chosen_number}")
    list_of_all_numbers = Sp.produce_number_list(chosen_number)
    print(f"The list of potential primes {list_of_all_numbers}")
    pairs_of_primes2 = Sp.all_pairs(list_of_all_numbers, chosen_number)
    final_list_of_pairs = Sp.remove_non_primes(pairs_of_primes2, list_of_all_numbers)
    if type(final_list_of_pairs) is list:
        print(final_list_of_pairs)
    else:
        pass

