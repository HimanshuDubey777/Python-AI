#1. Basics

def greet(name):
    return f"hello{name}"


#2. Parameters & Arguments

def calculate_margin(cost, revenue):
    profit = revenue - cost
    margin = profit * 100 / revenue
    return margin

calculate_margin(29,88)



def add (a,b):
    return a+b

def great(name="Rahul"):
    return f"Hello {name}"


def info(name,*,age,):
    return f"{name} is {age}"


####  *args and **kwargs


def total(*args):
    return sum (args)


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


total(1,2,3)
show_info(name="Rahul")





#4. Return Values


def stats(numbers):
    return min (numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = stats([1, 2, 3, 4])  # multiple return = tuple unpacking

#Returning multiple values (uses tuples, connects back to what you just learned)
#Early returns for validation



#5. Scope

x = 10 

def show():
    x = 52
    print(x)



def modify_global():
    global x
    print(x)


#6. Lambda (Anonymous Functions)

square = lambda x: x * x
print(square(5))


# Common with sorting/filtering

data =[(1,"b"),(2,"a")]
sorted(data, key=lambda x: x[1])


 #Higher-Order Functions


def apple_twice(func, value):
    return func(func(value))

apple_twice(lambda x: x + 3, 10) #16


nums = [1,2,3,4]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x%2 == 0, nums))

def calculate_margin(revenue: float, expences: float) -> float:
    profit = revenue - expences
    margin = profit *  100 / expences
    return margin


def calc_expence(exp1,exp2):
    return exp1+exp2

calc_expence(2,5)



def total_exp(rent,phnbill):
    return rent+phnbill

total_exp(phnbill=100,rent=32)

