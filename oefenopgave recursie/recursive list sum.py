#recursive list sum 
def main():
    getallen = ["642","643","234","765","123","453","823","574","140","112","652"]
    compleet = 0
    waarde(getallen, compleet)
    
def waarde(lijst, compleet):

    if len(lijst) > 0:
        getal = int(lijst[0])
        compleet += getal
        del lijst[0]
        waarde(lijst, compleet)

    elif len(lijst) == 0:
        print(compleet)  
    

main()
