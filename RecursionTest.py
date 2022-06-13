import timer
t = timer.Timer()


def recursive_function(all_pairs, all_primes, start_element):
    # This function is not implemented in the main program. It was written to see if a time saving could be made
    # with respect to the removal of pairs of values that contain primes (return value of all_pairs() (SerialPrime.py)
    # This function has been benchmarked up a input value of 1,000,000. A total of 95 seconds elapsed for this value.
    try:
        if type(all_pairs) is not list:
            raise ValueError
    except ValueError:
        pass
    else:
        items_to_remove = []
        for i in all_pairs:
            recursive(i, all_primes, start_element, items_to_remove)
        final_prime_list = [i for i in all_pairs if i not in items_to_remove]
        return final_prime_list


def recursive(i, all_primes, start_element, items_to_remove):
    # This is a recursive function designed to be called in recursive_function(). Not currently implemented.
    if int(i[1] % all_primes[start_element]) == 0:
        items_to_remove.append(i)
        return
    elif int(i[1] / all_primes[start_element] + 1) < all_primes[start_element]:
        return
    else:
        return recursive(i, all_primes, start_element + 1, items_to_remove)


def remove_some_primes_pairs(all_pairs, all_primes):
    # This function is not implemented in the main program. It is the first half of the function remove_non_primes2()
    # (SerialPrime.py). It assess if the 2nd element in the list all_pairs is a prime. It as a run as a direct
    # comparison to the function recursive_function() (this .py) which produces the same output for values up to
    # 1,000,000.
    # This function has been benchmarked up a input value of 1,000,000. A total of 90 seconds elapsed for this value.
    try:
        if type(all_pairs) is not list:
            raise ValueError
    except ValueError:
        pass
    else:
        items_to_remove = []
        for i in all_pairs:
            for j in all_primes:
                max_number = int(i[1]/j) + 1
                if i[1] % j == 0 and i[1] != j:
                    items_to_remove.append(i)
                    break
                elif j > max_number:
                    break
        final_prime_list = [i for i in all_pairs if i not in items_to_remove]
        return final_prime_list


if __name__ == '__main__':
    pass
