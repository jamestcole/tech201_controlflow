#Task 3 loops and lists
#Program1

count = 0

while count < 10:
    print("Hello World")
    count += 1


# Create a loop that iterates over each name in list_name and appends:
# Program 2

count2 = 0
list_names = []
program = True
print("This program will accept names for a register, between how many people are you expecting")
mi = int(input("The minimum number of people is:"))
ma = int(input("The maximum number of people is:"))
while program:
    name = input("Give a name")
    list_names.append(name)
    count2 += 1
    if count2 >= ma:
        print("We have the maximum number of people")
        program = False
    if count2 >= mi and count2 < ma:
        q = input("Would you like to continue the register?(y/n)")
        if q.lower() != "y":
            program = False
print("The following people have been admitted:")
for name in list_names:
    print(name)

#Make a loop that iterates over each name in list_name and format's it into
#lowercase in a new variable called list names lower
#Program 3
list_lower = []
print("Their names in lowercase are:")
for name in list_names:
    a = name.lower()
    list_lower.append(a)
for name in list_lower:
    print(name)

#Iterate over teh list of values to find if they are even

if count2%2 == 0:
    print("There are an even number of people")
if count2%2 != 0:
    print("There are an odd number of people")

print("END OF PROGRAMS")



