def print_kwargs(name = "Alice", power = "lazer"):
    print("Name:",name, ", power:",power)

def kwargs_print(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



# print_kwargs(power="Fly", name="Saktiman")
kwargs_print(name="PowerRanger", power="Fight", enimy="Dr.jackaal")