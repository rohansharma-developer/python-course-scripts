def prime(n):
    prime = True
    if n==0 or n==1:
        print("Neither prime nor composite")
    elif n==2:
        print("Prime Number")
    else:
        for num in range(2, int(n/2)):
            if n%num==0:
                print("Composite Number")
                prime=False
                break
        if prime:
            print("Prime Number")
number = int(input("Enter number to check: "))
prime(number)