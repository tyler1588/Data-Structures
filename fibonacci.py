def fibonacciRecursive(index):
    if index < 2:
        return index
    return fibonacciRecursive(index-1) + fibonacciRecursive(index-2)
# index = 1

print(fibonacciRecursive(7))