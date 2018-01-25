#afvinkopdracht 6

#fibonacci reeks.
import time
import re

def deel_een():
    lijst = []

    print("met dit programma kun je de fibonacci reeks berekenen.")

    for getal in range(int(input("geef het aantal keer dat het programma moet itteren: "))):
        print(fibo(getal))
        a = time.process_time()
        

    lijst = fibo_iteratie(lijst)
    b = time.process_time()
    for i in lijst:
        print(i)
    print("dit is de recursieve functie: ", a, "\ntegenover de iteratieve functie: ", b)

def fibo(waarde):
    if waarde == 0:
        return 0
    elif waarde == 1:
        return 1
    else:
        return fibo(waarde -1) + fibo(waarde - 2)

def fibo_iteratie(lijst):
    a, b = 0, 1
    
    for i in range(int(input("geef een getal: "))):
        a, b = b, a + b
        lijst.append(b)

    return lijst

    
#deel_een()

#DNA lengte berekenen
def deel_twee():
    tekst = "/home/cole/Documents/course 1/fasta bestanden/p53 mRNA drosophila melanogaster.fasta"
    sequentie = bestand_inlezen(tekst)
    print(recursief(sequentie))
    a = time.process_time()
    print(iteratief(sequentie))
    b = time.process_time()
    print(regular(sequentie))
    c = time.process_time()
    print("de recursieve functie doet er zo lang over: ", a,"\nde iteratieve functie doet er zo lang over: ", b,"\nde regulare expressie doet er zo lang over: ", c)
def bestand_inlezen(tekst):
    sequentie = ""
    for regel in open(tekst):
        if not regel.startswith(">"):
            sequentie += regel.strip()
    return sequentie

def recursief(invoer):
    #de code werkt, maar het bestand is zolang dat de computer het niet accepteert.
    letter = invoer[0]
    if not letter in "ATCG":
        return False
    if len(invoer) == 1:
        return True
    else:
        nieuw = invoer[1:]
        return recursief(nieuw)

        
        
def iteratief(sequentie):
    alles = 0
    for letter in sequentie:
        if letter in "ATCG":
            alles += 1
            
    if len(sequentie) == alles:
        return True
    else:
        return False 

def regular(sequentie):
    
    if not re.match("^[ATGC]+$", sequentie):
        return False
    else:
        return True
    
    
deel_twee()




    
