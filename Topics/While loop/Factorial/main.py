number = int(input())

factorial_number = 1
while number > 1:
    factorial_number *= number
    number -= 1

print(factorial_number)
