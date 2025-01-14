age = int(input("Enter pet age :" ))
spices = input("Enter spices name here :" )

if spices == "Dog" and age < 2 :
    food = "Puppy food"
elif spices == "Cat" and age > 5 :
    food = "Senior cat food"
else:
    food = "Unknow food"

print(food, "is for", spices)