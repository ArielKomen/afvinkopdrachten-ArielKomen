#ackermann's function 

   
def ackermann(m, n):
    
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n-1))


m = int(input("geef een getal: "))
n = int(input("geef nog een getal: "))
print(ackermann(m, n))



