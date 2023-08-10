1-write aphyton program to count the number 4 in a given list


numbers = [1, 2, 4, 4, 5, 4, 6, 7, 8, 4]
count = 0
for num in numbers:
    if num == 4:
        count += 1
print("Number of 4s in the list:", count)

/***********************************************/
2-
Write a Python program to test whether a passed letter is a vowel or not.


 numbers = [1, 2, 4, 4, 5, 4, 6, 7, 8, 4]
count = 0
for num in numbers:
    if num == 4:
        count += 1
print("Number of 4s in the list:", count)

/***********************************************/
3-




/************************************************/
4-Write a Python program which accepts the radius of a circle from the user and compute the area.


import pathlib

# Access a specific environment variable
variable_name = "MY_VARIABLE"
variable_value = pathlib.Path.environ.get(variable_name)

if variable_value is not None:
    print(f"The value of {variable_name} is: {variable_value}")
else:
    print(f"The environment variable {variable_name} is not set.")
 
/*********************************************/
5-Print the calendar of a given month and year


import calendar 
y=int(input("input the year : "))
m=int(input("input the month: "))
print(calendar.month(y,m))

/******************************************************The End :) *********************************************/