from datetime import date

class Human :
    def __init__(self ,name , birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_age (self):
        current_year = date.today().year
        return current_year - self.birth_year
    def introduce (self):
        print(f"Hi,My name is {self.name}.I am {self.get_age()}year old")


himanshu = Human ("Himanshu",2000) 
himanshu.get_age() 

harshit = Human ("Harshit",2006)
harshit.get_age()



