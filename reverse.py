# Iterative
def reverseString(str):
    i = len(str) - 1
    reverse = ""
    while i >= 0: 
        reverse += str[i]
        i -= 1
    return print(reverse)

reverseString('yoyo mastery')

