atoms = int(input())
final_quantity = int(input())
cycles = 0

while atoms >= final_quantity:
    cycles += 1
    if (cycles % 12) == 0:
        atoms /= 2

print(cycles)
