username = "Chaiaurcode"

def func():
    # username = "Chai"
    print(username)

print(username)
func()



#####################
x = 99
def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)


#####################
def func3():
    global x
    x = 12

func3()
print(x)


#####################
def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()


#####################
def f2():
    x = 12
    def f3():
        print("Inside f3 defination",x)
    return f3

myResult = f2()
myResult()



#####################
def demo(num):
    def actual(x):
        return x ** num
    return actual

f = demo(2)
g = demo(3)

print(f(3))
print(g(3))