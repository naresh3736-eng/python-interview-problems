# brute force

def fibo(n):
    if n <= 1:
        return
    i = 0
    j = 1
    result = []
    result.append(i)
    result.append(j)

    for a in range(2, n):
        sum = i + j
        result.append(sum)
        i = j
        j = sum

    return result


def fib_recursion(n):
    if n <= 1:
        return
    return fib_recursion(n-1) + fib_recursion(n-2)


cache = {}
def fib_memoization(n):
    if n in cache:
        return cache[n]

    if n == 1 or n == 2:
        value = 1

    else:
        value = fib_memoization(n-1) + fib_memoization(n-2)

    cache[n] = value
    return value

print fib_memoization(5)



