# num = [1, 2, 3, 4, 6, 7, 8, 9, 10]

# for x in num:
#     if x % 2 == 1:
#         print(x)


# username = str(input("Enter your username: "))
# username = username.lower()
# while username != "admin":
#     print("Invalid username. Please try again.")
#     username = input("Enter your username: ")
# print("Welcome, admin!")


# cars = {"Lexux", "BMW", "Mercedes", "Audi", "Porsche","Ferrari", "Lamborghini", "Maserati", "Bugatti", "Rolls-Royce"}

# cars[1] = "Tesla"
# for car in cars:
#     print(car)
# cars.insert(2, "Tesla")
# print(cars.count("Tesla"))
# cars.sort()
# print(cars)

# fruits = ["banana", "mango", "oranges", "carrot"]
# meats = ["chicken", "beef", "pork", "lamb"]
# vegatables = ["spinach", "kale", "broccoli", "cauliflower"]

# grocries = [fruits, meats, vegatables]
# print(grocries[0][1])
  
# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))


# for row in num_pad:
#     for num in row:
#         print(num, end="")
#     print()

# Dictionary

capital = {"USA" : "Washington",
              "UK" : "London",
                "France" : "Paris",
                "Germany" : "Berlin",
                "Italy" : "Rome",
                "Spain" : "Madrid",
                "Russia" : "Moscow",
           }
# print(capital.get("Russia"))
requsted_country = input("Enter a country: ")

while requsted_country not in capital:
    requsted_country = input("Enter a country: ")
    if requsted_country in capital:
        print(f"The capital of {requsted_country} is {capital[requsted_country]}")
print(f"The capital of {requsted_country} is {capital[requsted_country]}")

    


