# Using iterative approach

def add_digits_iterative(num):
    sum = 0
    while num > 0:
        remainder = num % 10
        sum += remainder
        num = num / 10

    return sum

print add_digits_iterative(575)


# Using recursion

def add_digits_recursion(num):
    if num == 0:
        return 0
    return num % 10 + add_digits_iterative(num/10)

print add_digits_recursion(575)


# Using brute force

def add_digits_bruteForce(num):
    sum = 0
    for i in str(num):
        sum += int(i)

    return sum

print add_digits_bruteForce(575)