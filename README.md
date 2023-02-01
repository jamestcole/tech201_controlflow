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

Here we use an elif statement, this can be broken down to else , if . if the first if statement doesn't run the second elif statement tests its conditions.

`elif film_rating.lower() == "pg":
    print("I'm afraid you cannot watch this movie , you are not old enough")`

Now we have expanded our elif statement to include or. So using the == operator if either of these conditions are true the indented code will run.

`elif film_rating.lower() == "12" or film_rating == "12a":
    print("12 rated movies may not be suitable for those under 12, supervision is recommended")`

many elif statements can be made in a row.

`elif film_rating.lower() == "15":
    print("You must be 15 to watch 15 rated movies in the cinema")`


`elif film_rating.lower() == "18":
    print("You must be 18 to watch 18 rated movies in the cinema")`

finally, there is an else statement. This will activate if non of the other statements run their code.

`else:
    print("This is not a correct rating, please use universal, pg, 12, 15, 18")`

In Python there are no 'switch statements' or 'case statements'

### Looping

A for loop is where you define an iterator number and cycle through data (list or dictionary) 'foreach' entry in that data structure.

Let's create  some lists and a dictionary. 

`list_data = [1, 2 , 3, 4, 5]`

`embedded_lists = [[1, 2, 3],[4, 5, 6]]`

`dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}`

With this for statement, we specify that each item in list_data is num. so this means , num initially is 1, then 2,3,4,5. We can do this by using
the in statement.

`for num in list_data:
    print(num * 2)`

Here we loop a for statement with another for statement. The first referes to each list in the
embedded list as data, the next opens data and iterates through each embedded list. This occurs before the code 
goes back to the last for statement and does this again for the next embedded list.
```
for data in embedded_lists:
    print(data)`
    for num in data:
        print(num)

```

Here we have a similar block of code for a dictionary.

```
for item in dict_data.values():
     for embed_value in item.values():
         print(embed_value)
     print(item)
```
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