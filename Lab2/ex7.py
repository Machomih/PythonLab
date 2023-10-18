def is_palindrome(number):
    ogl = 0
    copy = number
    while number:
        ogl = ogl * 10 + (number % 10)
        number = number // 10
    if ogl == copy:
        return 1
    return 0


def return_tuple(number_list):
    max_palindrome = 0
    count_palindrome = 0
    for n in number_list:
        if is_palindrome(n) == 1:
            count_palindrome += 1
            if n > max_palindrome:
                max_palindrome = n
    return count_palindrome, max_palindrome


print(return_tuple([11, 123, 121, 131, 999, 242, 500]))
