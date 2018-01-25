#recursive power method
def main():
    getal_1 = int(input("geef een getal: "))
    getal_2 = int(input("geef nog een getal, om het eerste getal tot de macht te doen: "))
    derde_getal = 0
    kracht(getal_1, getal_2, derde_getal)
    
def kracht(getal_1, getal_2, derde_getal):
    if getal_2 > 0:
        alfa = getal_1 * getal_2
        derde_getal += alfa
        getal_2 -= 1
        kracht(getal_1, getal_2, derde_getal)
    elif getal_2 == 0:
        print(derde_getal)
        
main()
