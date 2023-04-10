#Padlock Code Challenge
#Code hint
#code = 1 + 2 + 3 + 4 + … + 38 + 39 + 40

#Updating the code
code = 0
for i in range(1,41):
    print(i)

print("Code:")
print(code)

#To unlock the padlock, we will first find the sum of numbers from 1-41
first = 1
last = 40
n = 40

#Formular for sum of numbers
sum = n/2  * (first + last)

print(sum)