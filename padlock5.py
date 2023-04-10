code = 0
for digit1 in range(0,10):
    for digit2 in range(0,10):
        for digit3 in range(0,10):
            if digit1 == digit2 or digit2 == digit3 or digit1 == digit3: # check if at least two digits are equal
                code += 1
print(str(digit1)+str(digit2)+str(digit3))

print("Code:")
print(code)