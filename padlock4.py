code = 0

for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        for digit3 in range(0, 10):
            if (digit1 + digit2 + digit3) % 2 != 0:
                combination = str(digit1) + str(digit2) + str(digit3)
                print(combination)
                code += 1

print("Code: ", code)