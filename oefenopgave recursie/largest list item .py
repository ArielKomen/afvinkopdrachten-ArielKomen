def main():
    woorden = ["GGASEG","ATYAWS","ASGEA","ASGASG","ASGASEA","ASGASE","ASGGAE","GGTAGAE","ASDGEA","ATGEAS","ATC","ATCGA"]
    lijst_met_lengte = []
    lijsten(woorden, lijst_met_lengte)

def lijsten(lijst, lijst_met_lengte):
    
    
    if len(lijst) > 0:
        lengte = lijst[0]
        lijst_met_lengte.append(lengte)
        del lijst[0]
        lijsten(lijst, lijst_met_lengte)
    elif len(lijst) == 0:
        print(max(lijst_met_lengte))
    
main()
