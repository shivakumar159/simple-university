# write program to take a birth year and calculate the age

#birth_year = input("enter your birth year: ")

#age = 2026 - int(birth_year)

#print(f"your age is' {age}")

def divide(a, b):
    return a / b 
try:
 print(divide(10 ,2)) #output: 5.0

 print(divide(10 / 0)) # this will raise a zeroDivisionerror
except ZeroDivisionError:
 print("second paramiter cannot be zero")
