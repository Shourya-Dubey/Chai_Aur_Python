number = 29
is_Prime = True

if number > 1:
    for i in range(2, number):
        if (number % i == 0):
            is_Prime = False

print(is_Prime)