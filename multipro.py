from multiprocessing import Process, Pool, cpu_count
import timer
import UserInput

# This module is not currently implemented in the program, and is still in development. It is being developed to
# attempt to run some of the time-demanding parts of the code concurrently.


t = timer.Timer()


def prime1(x):
    prime_1 = ((6 * x) - 1)
    return prime_1


def prime2(x):
    prime_2 = ((6 * x) + 1)
    return prime_2


def parallel(x):
    z = 0
    number_of_elements = []
    for i in range(x):
        if z <= x:
            z = ((6 * i) + 1)
            #print(z)
            number_of_elements.append(z)
    el = len(number_of_elements)
    full_prime_list = []
    print(f"PC has {cpu_count()} cores. This calculation will be run with {cpu_count() - 2} cores")
    number_of_cores = cpu_count() - 2
    pool = Pool(processes=8)
    result1 = pool.map_async(prime1, range(0, el))
    result2 = pool.map_async(prime2, range(0, el))
    x = result1.get()
    y = result2.get()
    for i in range(len(y)):
        full_prime_list.append(x[i])
        full_prime_list.append(y[i])
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
            b = parallel(x)
            t.stop_timer()
            t.start_timer()
            c = list_of_primes2(x, b)
            t.stop_timer()
            return c
        except Exception as e:
            print(f"The following error has occurred: {e}")
    else:
        print("Program ended")


if __name__ == '__main__':
    print("")
    number = UserInput.user_input()
    answer = produce_primes(number)
    print(answer)
    """
    z = 0
    number_of_elements = []
    for i in range(number):
        if z <= number:
            z = ((6 * i) + 1)
            print(z)
            number_of_elements.append(z)
    print(len(number_of_elements))
    """
    pass
