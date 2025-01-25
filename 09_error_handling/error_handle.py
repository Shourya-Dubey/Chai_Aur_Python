file = open('test.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('test.txt', 'w') as file:
    file.write("Jai Shiv")