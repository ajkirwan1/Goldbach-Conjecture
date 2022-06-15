import timer
t = timer.Timer()

# This module contains the bulk of the code used to determine the a single pair of prime numbers and all prime
# numbers up a given user-defined value. All programs in this module are run by serial processing. Concurrent
# processing for several of the time-demanding functions in this module are to be developed and placed in
# multipro.py (not currently implemented), which is still in development.
# Several functions in this module have been benchmarked for numbers up to 1,000,000 for determining all
# prime pairs.


def function1(x):
    # Takes a single integer argument and applies the function ((6*x) - 1) to this value. Returns this value.
    prime_1 = ((6 * x) - 1)
    return prime_1


def function2(x):
    # Takes a single integer argument and applies the function ((6*x) + 1) to this value. Returns this value.
    prime_2 = ((6 * x) + 1)
    return prime_2


def full_list(x):
    # Takes a single argument: the valid user input value (see user_input(); UserInput.py). To every integer in the
    # range of 0 to this user input value, function1() and function2() are applied, providing that the output of
    # function1() of function2() is less than or equal to the value of the user input. Outputted values that fit
    # this criteria are appended to a list (full_list). Hence, this list will contain all primes less than the value
    # inputted by the user (apart from the integers 2 and 3).
    full_list = []
    z = 0
    for i in range(x):
        if z <= x:
            set1 = function1(i)
            set2 = function2(i)
            full_list.append(set1)
            full_list.append(set2)
            z = ((6 * i) + 1)
    return full_list


def adjust_list(x, full_list):
    # Takes two arguments: x = user_input value; full_list = return value from the function full_list(). This function
    # removes values less than 0, values greater than the user input, and the integer value 1 from full_list() return
    # list. It additionally adds the integer values 2 and 3 to full_list, and returns a new list called adjusted_list.
    items_to_remove = []
    for i in full_list:
        if i < 0 or i > x or i == 1:
            items_to_remove.append(i)
    adjusted_list = [i for i in full_list if i not in items_to_remove]
    adjusted_list.insert(0, 3)
    adjusted_list.insert(0, 2)
    return adjusted_list


def produce_number_list(x):
    # This function takes a single argument: x = user_input value. The function produce_primes() is built to to process
    # full_list and adjust list and simultaneously process the error where the input user value is None. The return
    # value is a list of all numbers -  between 0 and the number chosen by the user -  that fits the equations
    # given in function1() and function(), and that are additionally amended by adjust_list().
    # **** This function may not be necessary. Could look at removing this in future dev ****
    if x is not None:
        try:
            b = full_list(x)
            number_list = adjust_list(x, b)
            return number_list
        except Exception as e:
            print(f"The following error has occurred: {e}")
    else:
        print("Program ended")


def all_pairs(y, chosen_number):
    # This function takes 2 arguments: y = the outputted list of numbers from the function produce_number_list()
    # finds all pairs of numbers in the list 'adjusted_list' that is returned from the function
    # adjust_list(), and returns a list of pairs. Note that not all of these numbers are necessarily prime numbers.
    # This function has been benchmarked up a input value of 1,000,000. A total of 245 seconds elapsed for this value.

    try:
        if type(y) is not list:
            raise ValueError
    except ValueError:
        pass
    else:
        reverse_list = reversed(y)
        reversed_list = list(reverse_list)

        all_pairs = []
        for i in range(len(y)):
            if i < (int((len(y) +1) / 2)):
                if (y[i] + reversed_list[i]) == chosen_number:
                    temp = (y[i], reversed_list[i])
                    all_pairs.append(temp)
                elif (y[i] + reversed_list[i]) < chosen_number:
                    j = y.index(y[i])
                    for j in range(y.index(y[i]) + 1, len(y)):
                        if y[j] + reversed_list[i] == chosen_number:
                            temp = [y[j], reversed_list[i]]
                            all_pairs.append(temp)
                            break
                        if y[j] + reversed_list[i] > chosen_number:
                            break
                elif (y[i] + reversed_list[i]) > chosen_number:
                    j = reversed_list.index(reversed_list[i])
                    for j in range(reversed_list.index(reversed_list[i]) + 1, len(reversed_list)):
                        if y[i] + reversed_list[j] == chosen_number:
                            temp = [y[i], reversed_list[j]]
                            all_pairs.append(temp)
                            break
                        if y[i] + reversed_list[j] < chosen_number:
                            break
            else:
                break
        return all_pairs


def single_pair(y, chosen_number):
    # This function is used to produce a single pair of prime numbers.
    try:
        if type(y) is not list:
            raise ValueError
    except ValueError:
        pass
    else:
        reverse_list = reversed(y)
        reversed_list = list(reverse_list)
        pairs = []
        count = 0
        for i in y:
            if y.index(i) < (int(len(y) / 2) + 1) and count != len(y):
                for j in reversed_list:
                    if i + j < chosen_number:
                        break
                    if i + j == chosen_number:
                        count = 0
                        temp = [i, j]
                        for k in y:
                            if j % k == 0 and j != k:
                                break
                            else:
                                count += 1
                        if count == len(y):
                            break
                    if i + j > chosen_number:
                        pass
            else:
                break
        pairs.append(temp)
        return pairs


def remove_non_primes(all_pairs, all_primes):
    # This function has been benchmarked up a input value of 1,000,000. A total of 289 seconds elapsed for this value.
    # For a value of 1,000,000, both remove_non_primes2() and remove_non_primes() return the same set of lists.
    try:
        if type(all_pairs) is not list:
            raise ValueError
    except ValueError:
        pass
    else:
        items_to_remove = []
        for i in all_pairs:
            for j in all_primes:
                if i[1] % j == 0 and i[1] != j:
                    items_to_remove.append(i)
                    break
                if i[0] % j == 0 and i[0] != j:
                    items_to_remove.append(i)
                    break
        final_prime_list = [i for i in all_pairs if i not in items_to_remove]

        return final_prime_list


def remove_non_primes2(all_pairs, all_primes):
    # This function has been benchmarked up a input value of 1,000,000. A total of 268 seconds elapsed for this value.
    # For a value of 1,000,000, both remove_non_primes2() and remove_non_primes() return the same set of lists.
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
        for i in all_pairs:
            for j in all_primes:
                if i[0] % j == 0 and i[0] != j:
                    items_to_remove.append(i)
                    break
                elif i[0] == j:
                    break
        final_prime_list = [i for i in all_pairs if i not in items_to_remove]

        return final_prime_list

