def sum_array(array):
    sum = 0
    for a in array:
        sum += a

    '''Return sum of all items in array'''
    return sum
def fibonacci(n):

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    '''Return nth term in fibonacci sequence'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    '''Return n!'''
def reverse(word):
    reverse_word = word[::-1]

    return reverse_word

    '''Re

    turn word in reverse'''
