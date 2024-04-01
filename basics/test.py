def mult(n):
    while n>0:
        if n%2 == 0:
            print(n)
            mult(n-1)
        else:
            mult(n-1)
        return

mult(66)

