pos = int(input("Enter position of fibonacci number to find: "))
n1 = 0
n2 = 1
count = 0
while count < pos:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
    
print(n1)