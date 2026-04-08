# print("I Love Pizza")

# #Strings
# last_name = "John"
# food = "rice"
# password = '123456789'

# print(f"Hello! {last_name},your favourite {food} is ready!")

# print(f" Your account password is {password}")

# #Integers

# age = 30
# quantities = 100
# num_of_police = 100

# print (f"You are {age} years old!")
# print (f"You bought {quantities} pack of biscuiut")
# print(f"There are {num_of_police} numbers of police")

# # Float

# cost = 99.99
# speed = 2.2
# gpa = 3.4

# print(f"The shoe cost ${cost}")
# print(f"The jets top speed is mach {speed} ")
# print(f" Yor result is: {gpa} GPA")

# # Boolean
# is_teacher = False

# if is_teacher :
#     print(f"You are a teacher, welcome")
# else:
#     print(f"You are not a teacher, Bye!!")

#     # # TypeCasting

    # name = "F-35A"
    # age = 6
    # speed = 1.2
    # is_fighter = True

    # print(type(age))

    # speed = int(speed)
    # print(speed)

    # age = float(age)
    # print(age)

    # # input   A function that prompt user to  enter data and returns data as string 

    # name = input("What is your name ?: ")
    # age = float(input("How old are you?: "))
   
  

   #22 print(f"Hello {name}, Your {age} is below the limit, must be above 18")

# Area fo a rect cal

# length = float(input("Enter the length ?: "))
# width = float(input("Enter the width ?: "))

# area = length * width

# print(f"The area of this rectangle is: {area}cm²")

numbers = [1, 2, 3, 4, 5, 6, 6, 7, 7, 7, 8, 9, 10]

# for even_numbers in numbers:
#     if even_numbers % 2 == 0 :
#         print(even_numbers, end=" ")

# update = tuple(numbers)
# print(update)

# functions
# it is a block of reusable codew

# song = False

# while  song != False:
#     print("Happy Birthday to You")

# else:
#     print("It's not your birthday")

# def happy_birthday(name, age ):
#     print(f"Happy Birthday to {name} ") 
#     print(f"You are now  {age} years old" )
#     print("Happy Birthday!!!")
#     print()

# happy_birthday("chijioke", 22)
# happy_birthday("Jude", 100)
# happy_birthday("Larryson", 101)

# def display_invoice(username, amount, due_date):
#     print(f"Hello!! {username}, Here is your invoice 👇 ")
#     print(f"Your total :${round(amount, 3)}  with a due date of{due_date}")

# display_invoice("silentxbt", 10000000, "11-12-2001")


#Return statement
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name("John", "Kenenchukwu")

# print(full_name)

# Module . its a python file that has coses you  want to include in your code 
# Modeles are included using "import" or  you can create your own  module

# print(help("list"))

# Varaible scope is where a varaiable is visible and accessible 
# Scope Resolution - (LEGB) Local, enclose , global built in

#Exception handling is an event that interrupt the flow of a program (
#  ZeroDivisionError, TpeError, ValueError)

import json

employee = {
   "Mark" : "Jude",
   "job" : "Engineer",
   "Marital" : "Married",
   "Kids":"two"
}


file_path = 'output.json'


try:
    with open(file_path, 'w') as file:
         json.dump(employee, file, indent=4)
         print(f"json file {'file_path'} was created")
   
    
except FileExistsError: 
    print("File already exists")
    
