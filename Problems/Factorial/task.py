number = int(input().strip())
output = 1

while number != 0:
    output *= number
    number -= 1

print(output)
