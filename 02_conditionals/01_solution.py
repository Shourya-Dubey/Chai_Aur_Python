age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Tenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")