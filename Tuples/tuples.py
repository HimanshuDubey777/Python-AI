#Tuple vs List — the key difference


my_list = [1,2,3]
my_list[0]=233
my_list.append(4)

my_tuple = (1,2,3)
my_tuple[0]=100
my_tuple.append(4)  # type error



t = ( 20 ,30 ,40 ,50)


print(t[0])
print(t[1])
print(t[3])
print(t[-1])
print(t[1:3])
print(len(t))
print(30 in t)



#Real-world / production-style examples



"""
1. Returning multiple values from a function
This is the #1 real-world use of tuples.
"""

def get_user_info():
    name = "Himanshu"
    age = 25
    city = "Locknow"
    return name, age, city

name , age , city = get_user_info()
print(name,age,city)



purple = (128 ,0 ,128)
purple[0]

r,g,b = purple
print(g)



def devide(a,b):
    if b == 0:
        return  False ,None , "devision by zero is not allowed"
    return  True, a/b , None
success , result , error = devide(10,0)
if success:
    print("Result:" ,result)
else:
    print("Error:",error)




