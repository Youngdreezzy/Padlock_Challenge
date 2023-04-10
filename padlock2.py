#Padlock 2 Challenge
#Code hint: code = Total number of 3-digit combinations where digit1 < digit2 < digit3

code = 0
#
for digit1 in range(0,10):
  for digit2 in range(digit1+1,10):
    for digit3 in range(digit2+1,10):
       code += 1

print("Code:")
print(code)