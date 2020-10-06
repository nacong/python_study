n=int(input("몇 개?"))
num1 = []
 
for i in range(n):
    num1.append(0)

num2 = input("순서! : ").split(' ')

for i in range(n):
    num1[i] = num2[i]

sum = 0
result = 0

for i in range(n-1):
    sum = abs(int(num1[i]) -int(num1[i+1]))
    result += sum

print(result)
