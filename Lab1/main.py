def first_task():
    print('input numbers:')
    number_string = input()
    number_list = number_string.split()
    numbers = ([int(number) for number in number_list])
    gcd = find_gcd(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        gcd = find_gcd(gcd, numbers[i])
    print('result is:', gcd)


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def second_task():
    print('input string:')
    string = input()
    print('number of vowels is:', count_vowels(string))


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(string.count(vowel) for vowel in vowels)
    return count


def third_task():
    print('input first string:')
    first = input()
    print('input second string')
    second = input()
    print('Number of appearances:', second.count(first))


def fourth_task():
    print('input string:')
    string = input()
    result = [string[0].lower()]
    for letter in string[1:]:
        if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result.append('_')
            result.append(letter.lower())
        else:
            result.append(letter)
    print('result is:', ''.join(result))


def fifth_task():
    matrix = [['f', 'i', 'r', 's', '1'],
              ['n', '_', 'l', 't', '2'],
              ['o', 'b', 'a', '_', '3'],
              ['h', 't', 'y', 'p', '4'],
              ['n', '_', 'l', 't', '5']]
    n = len(matrix)
    m = len(matrix[0])
    result = ''
    for turn in range(0, n // 2):
        for j in range(turn, m - turn):  # turn, m-turn
            result += matrix[turn][j]  # turn
        for i in range(turn + 1, n - turn):  # turn+1, n-turn
            result += matrix[i][m - turn - 1]  # m-turn-1
        for j in range(m - turn - 2, turn - 1, -1):  # m-turn-2, turn-1
            result += matrix[n - turn - 1][j]  # n-turn-1
        for i in range(n - turn - 2, turn, -1):  # n-turn-2, turn
            result += matrix[i][turn]  # turn
    if n / 2 != n // 2:
        middle = (n - 1) // 2
        result += matrix[middle][middle]
    print('result is:', result)


def sixth_task():
    number = int(input())
    copy = number
    palindrome = 0
    while copy:
        palindrome = palindrome * 10 + copy % 10
        copy //= 10
    print('the answer is:', number == palindrome)


def seventh_task():
    string = input()
    numbers = '1234567890'
    final_number = 0
    for index in range(0, len(string) - 1):
        if string[index] in numbers:
            final_number = final_number * 10 + int(string[index])
        if string[index+1] == ' ':
            break
    print("Number extracted is:", final_number)


def eighth_task():
    number = str(bin(int(input())))
    counter = 0
    for digit in number:
        if digit == '1':
            counter += 1
    print('The number has:', counter, 'bits of 1')


def ninth_task():
    string = input().lower()
    letters = []
    count_list = []
    for letter in string:
        if letter not in letters and letter not in ' ,.-_':
            letters.append(letter)
            count_list.append(string.count(letter))
    max_count = max(count_list)
    max_char = letters[count_list.index(max_count)]
    print('The most common letter in string is:', max_char, ':', max_count)


def tenth_task():
    string = input()
    counter = 0
    for index in range(0, len(string) - 1):
        if string[index] == ' ' and string[index + 1] != ' ':
            counter += 1
    print('there are', counter + 1, 'words')


# first_task()
# second_task()
# third_task()
# fourth_task()
# fifth_task()
# sixth_task()
seventh_task()
# eighth_task()
# ninth_task()
# tenth_task()
