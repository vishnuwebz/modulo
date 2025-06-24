# 3 lucky digit checker

num = int(input("Enter a number: "))

last_digit = num % 10

if last_digit in [3, 7, 9]:
    print("You're lucky!")
else:
    print("Better luck next time.")