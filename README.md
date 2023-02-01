# tech201_controlflow
tech201_controlflow

## Control Flow

Control Flow -> Flow through a particular decision process

### if statement
if statements are some of the most important statements used in python, they are needed to tell the program to take a certain action after conditionals.

Let's define a variable.

`age = 19`

This will print the string in the print statement as our variable age is equal to 19 which meets the conditional, the if statement activates the indented code if this conditional evaluates as true.

`if age >= 18:
    print("You are the correct age to watch this file and can buy a ticket")`

Note, there is no false here, if it is not true the code simple continues. This does not produce an error.
We can write another if statement to print a line in the event the age is smaller than 18, however this is not the ideal way to code this.

`if age < 18:
    print("I'm afraid you cannot watch this movie , you are not old enough")`



### elif and else

We can first define a variable we want to use.

`film_rating = "universal"`

Here we use an if statement, whatever is contained in the indented line begins to run if the condition is met. Here we use a == operater which returns true if the two sides are equal.
The film_rating uses the .lower() method as we do not care about the case of the string.

`if film_rating.lower() == "universal":
    print("All age groups can watch this film")`



`elif film_rating.lower() == "pg":
    print("I'm afraid you cannot watch this movie , you are not old enough")`


`elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12, supervision is recommended")`


`elif film_rating.lower() == "15":
    print("You must be 15 to watch 15 rated movies in the cinema")`


`elif film_rating.lower() == "18":
    print("You must be 18 to watch 18 rated movies in the cinema")`


`else:
    print("This is not a correct rating, please use universal, pg, 12, 15, 18")`



# In Python there are no 'switch statements' or 'case statements'

# Looping

# A for loop is where you define an iteraor number and cycle through data (list or dictionary) 'foreach' entry in that data structure.

# Creating a for loop

list_data = [1, 2 , 3, 4, 5]

embedded_lists = [[1, 2, 3],[4, 5, 6]]

dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

#for num in list_data:
#    print(num * 2)

# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)
#     print(item)

for items in dict_data.values():
    print(items["money"])

# please see python documentation for more you can do with dictionaries and loops

list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found 3")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon")