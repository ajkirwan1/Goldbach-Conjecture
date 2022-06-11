import Error
import timer
import UserInput
t = timer.Timer()
from multiprocessing import Process, Pool,cpu_count


def prime1(x):
    prime_1 = ((6 * x) - 1)
    return prime_1


def prime2(x):
    prime_2 = ((6 * x) + 1)
    return prime_2


def list_of_all_primes(x):

    full_prime_list = []
    z = 0
    for i in range(x):
        if z <= x:
            prime_1 = prime1(i)
            prime_2 = prime2(i)
            full_prime_list.append(prime_1)
            full_prime_list.append(prime_2)
            z = ((6 * i) + 1)

    return full_prime_list


def remove_unwanted_numbers(x, full_prime_list):
    items_to_remove = []
    for i in full_prime_list:
        if i < 0 or i > x or i == 1:
            items_to_remove.append(i)
    final_prime_list = [i for i in full_prime_list if i not in items_to_remove]
    final_prime_list.insert(0, 3)
    final_prime_list.insert(0, 2)
    return final_prime_list


def produce_primes(x):
    if x is not None:
        try:
            b = list_of_all_primes(x)
            c = remove_unwanted_numbers(x, b)
            return c
        except Exception as e:
            print(f"The following error has occurred: {e}")
    else:
        print("Program ended")


def prime_pairs2(y, chosen_number):
    try:
        if type(y) is not list:
            raise ValueError
    except ValueError:
        pass
    else:
        t.start_timer()
        reverse_list = reversed(y)
        reversed_list = list(reverse_list)

        pairs = []
        for i in range(len(y)):
            if i < (int(len(y) / 2)):
                if (y[i] + reversed_list[i]) == chosen_number:
                    temp = (y[i], reversed_list[i])
                    pairs.append(temp)
                elif (y[i] + reversed_list[i]) < chosen_number:
                    j = y.index(y[i])
                    for j in range(y.index(y[i]) + 1, len(y)):
                        if y[j] + reversed_list[i] == chosen_number:
                            temp = [y[j], reversed_list[i]]
                            pairs.append(temp)
                            break
                        if y[j] + reversed_list[i] > chosen_number:
                            break
                elif (y[i] + reversed_list[i]) > chosen_number:
                    print("BIGGGGERRRR")
                    print(y[i])
                    print(reversed_list[i])
            else:
                break
        return pairs


def remove_non_primes(pairs_of_primes2, all_primes):
    try:
        if type(pairs_of_primes2) is not list:
            raise ValueError
    except ValueError:
        pass
    else:
        items_to_remove = []
        t.start_timer()
        for i in pairs_of_primes2:
            for j in all_primes:
                if i[1] % j == 0 and i[1] != j:
                    items_to_remove.append(i)
        final_prime_list = [i for i in pairs_of_primes2 if i not in items_to_remove]

        return final_prime_list



if __name__ == '__main__':
    t.start_timer()
    chosen_number = UserInput.user_input()
    t.stop_timer()
    t.start_timer()
    all_primes = produce_primes(chosen_number)
    t.stop_timer()
    t.start_timer()
    pairs_of_primes2 = prime_pairs2(all_primes, chosen_number)
    t.stop_timer()
    final_list_of_pairs = remove_non_primes(pairs_of_primes2, all_primes)
    if type(final_list_of_pairs) is list:
       print(final_list_of_pairs)
    else:
        pass
