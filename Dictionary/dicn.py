

student ={
    "name": "Himanshu Dubey",
    "age": 20,
    "role": "Ai Engineer"
}

print(student["age"])



car = {
    "Brand": "BMW",
    "Model": "X5",
    "year": 2023
}

print(car["Brand"])
print(car["Model"])
print(car["year"])


#Difference Between List and Dictionary

Fruits =["Apple","Banana","Mango"]
print(Fruits[0])


fruits = {
    "frist": "apple",
    "second": "banana",
    "third": "mango"
}
print(fruits["frist"])



student = {}

student["Name"]= "Himanshu Dubey"
student["age"]=20

print(student["Name"])





student = {
    "name": "Himanshu",
    "age": 20
}

student["role"] = "Ai Engineer"

print(student)


student = {
    "name": "Himanshu",
    "age": 20
}

del student["age"]


print(student)



car = {
    "name ":"BMW",
    "prize": 400000

}
print(car.get("name"))



student = {
    "name": "pooja",
    "age": 24
}

print(student.keys())



student = {
    "name": "pooja",
    "age": 24
}

print(student.values())


student = {
    "name": "pooja",
    "age": 24
}

print(student.items())




student = {
    "name": "Himanshu",
    "role": "Ai Engineer"
}

for key in student:
    print(key)


student = {
    "name": "Himanshu",
    "role": "Ai Engineer"
}

for value in student.values():
    print(value)


#key and value together

student = {
    "name": "Himanshu",
    "role": "Ai Engineer"
}

for key, value in student.items():
    print(key, value)


# neated Dictionary


students = {

    "student1": {
        "name": "Himanshu",
        "age": 24
    },
    "studet2":{
        "name": "pooja",
        "age": 24
    }

}

print(students["student1"]["name"])


#Dictionary Inside a List

#Very common in APIs.


students = [
    {"name":"Himanshu","age":24},
    {"name":"pooja","age":24},
    {"name":"jack","age":25}
]

print(students[2]["name"])


student = {
    "name": "Himanshu",
    "age": 23
}

print(student["name"])



#List Inside a Dictionary


company = {
    "name": "IBM",
    "employees": [
        "himanshu",
        "pooja",
        "jack"
    ]
}

print(company["employees"][1])



company = {
    "name": "Google",
    "employees": [
        "jack",
        "leechh",
        "rest"
    ]
}

print(company["employees"][2])





response = {
    "id": 12,
    "name": "laptop",
    "price":2000,
    "stock": 23
}

print(response["name"])
print(response["id"])



user = {
    "name": "atul",
    "id": 1,
    "skills": [
        "python",
        "java",
        "docker",
        "ansible"
    ]
}

print(user["skills"][2])


financials = {

    "Q1": {"revenue":100, "expenses": 40},
    "Q2": {"revenue":150, "expenses": 60},
    "Q3": {"revenue":200, "expenses": 80},
}
for quarter, data in financials.items():
   margin = (data["revenue"]-data["expenses"]) / data["revenue"]*100
   print(f"{quarter} margin: {margin:.2f}%")







































