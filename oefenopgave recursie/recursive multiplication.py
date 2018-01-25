#recursive multiplication

def main():
    x = int(input("geef een getal: "))
    y = int(input("geef een getal: "))
    z = 0
    keer(x, y, z)

def keer(x, y, z = 0):
    if x > 0 and y > 0:
        z += y
        print(z)
        keer((x-1), (y), z = z)
        


main()
