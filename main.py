
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
        if i < 0 or i > x:
            items_to_remove.append(i)
    final_prime_list = [i for i in full_prime_list if i not in items_to_remove]
    final_prime_list.insert(1, 3)
    return final_prime_list


def produce_primes(x):
    if x is not None:
        try:
            t.start_timer()
            b = list_of_primes1(x)
            t.stop_timer()
            t.start_timer()
            c = list_of_primes2(x, b)
            t.stop_timer()
            return c
        except Exception as e:
            print(f"The following error has occurred: {e}")
    else:
        print("Program ended")


def prime_pairs(y):

    reverse_list = reversed(y)
    reversed_list = list(reverse_list)

    pairs = []
    for i in y:
        if y.index(i) < (int(len(y) / 2) + 1):
            for j in reversed_list:
                if i + j < number:
                    break
                if i + j == number:
                    temp = [i, j]
                    pairs.append(temp)
                    break
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
                if (y[i] + reversed_list[i]) == number:
                    temp = (y[i], reversed_list[i])
                    pairs.append(temp)
                elif (y[i] + reversed_list[i]) < number:
                    if y[i+1] + reversed_list[i] == number:
                        temp = (y[i+1], reversed_list[i])
                        pairs.append(temp)
                    else:
                        pass
                elif (y[i] + reversed_list[i]) > number:
                    print("Number is more")
            else:
                break
        t.stop_timer()
        return pairs




if __name__ == '__main__':

    number = UserInput.user_input()
    y = produce_primes(number)
    x = prime_pairs2(y)
    if type(x) is list:
        print(x)
    else:
        pass

