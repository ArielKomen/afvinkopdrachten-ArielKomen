#recursive lines

def main():
    n = int(input("geef een getal: "))
    i = 1
    regel(n, i)
    
def regel(n, i):
    if n > 0:
        print(i * "*")
        regel(n-1, i+1)
    else:
        print("geef een groter getal dan 0")
    
        


main()
