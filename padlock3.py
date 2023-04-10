code = 0 
 # initialize a variable to keep track of the count of valid combinations
for digit1 in range(0, 10, 2):  
    for digit2 in range(0, 10, 2):
        for digit3 in range(0, 10, 2):
            code += 1  
print("Code:", code)
