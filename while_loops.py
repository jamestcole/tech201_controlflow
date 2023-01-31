# While loops

# While loops monitor data rather than iterate

x = 0

# while x < 10:
#     print(f"It's working > {x}")
#     x += 1 #incrementer

#using break

# while x < 10:
#     print(f"It's working > {x}")
#     if x == 4:
#         break
#     x += 1
#
# print(x) # 4

# Asking for someone's age
# This can either be an int (20) or string (twenty)
# age = input("What is your age?")
# #
# # print(f"your age is {age}")

user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) <118:
        user_prompt = False
    else:
        print("Please provide your answer in digits and below 118")

print(f"Your age is {age}")
