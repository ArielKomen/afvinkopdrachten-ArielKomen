#recursive printing

def main():
    getal = int(input("geef een heel getal: "))
    printen(getal)
    
def printen(getal):
    if getal == 0 or getal == 1:
        return "het getal is: ", getal
    elif getal > 0 or getal > 1:
        printen(getal - 1)
        print(getal)

main()
