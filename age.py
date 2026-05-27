class ageException(Exception):
    def ___init___(self, value):
        self.value = value
    def __str__(self):
        return (f"age: {self.value} is not valid")
    
try:
    age = int(input("enter your age: "))
    if age < 0 or age > 120:
        raise ageException(age)
    print(f"your age is: {age}")
except ageException as e:
    print(e)
else:
    print("age is valid.")
finally:
    print("age validation completed")
               