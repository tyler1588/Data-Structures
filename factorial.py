def findFactorialRecursive(number):
    if number <= 1:
        return 1
    return number * findFactorialRecursive(number - 1)

def findFactorialIterative(number):
    product = number
    number -= 1
    while number > 0:
        product *= number
        number -= 1
    return print(product)

print(findFactorialRecursive(5))