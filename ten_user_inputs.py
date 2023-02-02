# amount = 0
# number = 0
# print("I will ask you for ten numbers and return the average")
# while True:
#     amount += 1
#     number += int(input("give me a number:"))
#     if amount == 10:
#         break
#
# print(f"the average value of your numbers is: {number/10}")

total = 0
for i in range(10):
    total += int(input("Enter a Number: "))
print(f"the total of your inputs is {total/10}")
