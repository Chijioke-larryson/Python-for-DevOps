# # Shopping Cart

# item = input("What item do you want to buy ?: ")
# price = float(input("What price do you want ?: "))
# quantity = int(input("How many do you want?: "))
# total = price * quantity

# print(F"Your {item} cost ${total}")

# Madlib Game
# noun1 = input("Enter a noun (place, name, animal): " )
# verb1 = input("Enter a verb (action) ending with 'ing': ")
# adjective1 = input("Enter an adjective (description): ")
# adjective2 = input("Enter an  adjective (description)")

# print(f"I went to the {noun1} today")
# print(f"In the {noun1} people where {verb1}")
# print(f"In {noun1} the place is {adjective1}")
# print(f"I was {adjective2}")

#Circumference of a circle 
import math

# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is:  {round(circumference, 3)}cm")


# radius = float(input("Enter the radius of a circle: "))

# Area = math.pi * pow(radius, 2)

# print(f"The Area of the circle is: {round(Area, 3)}")

A = float(input("Enter length of side A: "))
B = float(input("Enter length of side B: "))
sum =  pow(A, 2) + pow(B, 2)
result = math.sqrt(sum)
print(f"The hypothesis of the triangle is: {round(result,2)}cm")