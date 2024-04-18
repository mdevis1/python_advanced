def recursive(n):
    if n < 1 :
        return 1
    else:
        number = n * recursive(n-1)
        return number


print(f'This is the factorial of 5 : {recursive(5)}')