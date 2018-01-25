#sum of numbers
def main():
    getal = int(input("geef een getal: "))
    tweede_getal = 0
    derde_getal = 0
    integer(getal, tweede_getal, derde_getal)

def integer(waarde, tweede_getal, derde_getal):
    
    if waarde > 0:
        tweede_getal += 1
        derde_getal += tweede_getal
        integer(waarde-1, tweede_getal, derde_getal)
    elif waarde == 0:
        print(derde_getal)
        
    

main()
