def is_prime(number):
    if number < 2:
        return 0
    if number % 2 == 0 and number != 2:
        return 0
    for i in range(3, number // 2, 2):
        if number % i == 0:
            return 0
    return 1


def return_primes(number_list):
    prime_list = []
    for i in number_list:
        if is_prime(i) == 1:
            prime_list += [i]
    return prime_list


print(return_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
