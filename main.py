
import Error
import timer
import UserInput
t = timer.Timer()
import SerialPrime as sp


from multiprocessing import Process, Pool,cpu_count

def prime1(x):
    prime_1 = ((6 * x) - 1)
    return prime_1


def prime2(x):
    prime_2 = ((6 * x) + 1)
    return prime_2


def list_of_primes1(x):

    full_prime_list = []
    z = x
    for i in range(x):
        if z <= x:
            prime_1 = prime1(i)
            prime_2 = prime2(i)
            full_prime_list.append(prime_1)
            full_prime_list.append(prime_2)
            z = ((6 * i) + 1)

    return full_prime_list


def list_of_primes2(x, full_prime_list):
    items_to_remove = []
    for i in full_prime_list:
        if i < 0 or i > x or i == 1:
            items_to_remove.append(i)
        elif i > 5 and i % 5 == 0:
            items_to_remove.append(i)
        elif i > 7 and i % 7 == 0:
            items_to_remove.append(i)
    final_prime_list = [i for i in full_prime_list if i not in items_to_remove]
    final_prime_list.insert(0, 3)
    final_prime_list.insert(0, 2)
    return final_prime_list


def produce_primes(x):
    if x is not None:
        try:
            #t.start_timer()
            b = list_of_primes1(x)
            #t.stop_timer()
            #t.start_timer()
            c = list_of_primes2(x, b)
            #t.stop_timer()
            return c
        except Exception as e:
            print(f"The following error has occurred: {e}")
    else:
        print("Program ended")


def prime_pairs(y):
    t.start_timer()
    reverse_list = reversed(y)
    reversed_list = list(reverse_list)

    pairs = []
    for i in y:
        if y.index(i) < (int(len(y) / 2) + 1):
            for j in reversed_list:
                if i + j < number:
                    break
                if i + j == number:
                    temp =(i, j)
                    pairs.append(temp)
                    break
    t.stop_timer()
    return pairs


def prime_pairs2(y):
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
                #print(f"The numbers are {y[i]} and {reversed_list[i]}")
                if (y[i] + reversed_list[i]) == number:
                    temp = (y[i], reversed_list[i])
                    pairs.append(temp)
                elif (y[i] + reversed_list[i]) < number:
                    #print(f"The current index of y is: {y.index(y[i])}")
                    j = y.index(y[i])
                    for j in range(y.index(y[i]) + 1, len(y)):
                        #print(f"The numbers are {y[j]} and {reversed_list[i]}")
                        if y[j] + reversed_list[i] == number:
                            temp = (y[j], reversed_list[i])
                            pairs.append(temp)
                            #print("True")
                            break
                        if y[j] + reversed_list[i] > number:
                            break
            else:
                break
        t.stop_timer()
        return pairs


def final_remove():
    pass


if __name__ == '__main__':
    #UserInput.user_input()
    chosen_number = UserInput.user_input()
    all_primes = sp.produce_primes(chosen_number)
    pairs_of_primes2 = sp.prime_pairs2(all_primes, chosen_number)
    final_list_of_pairs = sp.remove_non_primes(pairs_of_primes2,all_primes)

    if type(final_list_of_pairs) is list:
       print(final_list_of_pairs)
    else:
        pass

