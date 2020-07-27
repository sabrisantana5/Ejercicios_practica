#Program that calculates the angle between the hands of the clock
def calculaAngulo(horas: int, minutos: int, segundos: int):
    
    if(horas>23 or minutos >60 or segundos >60):
        return -1
    elif(horas<0 or minutos <0 or segundos <0):
        return -1
    else:
        ManecillaHoras = horas*30 + (minutos/60)*30 + ((segundos/60)/60)*30
        print("La manecilla de horas está en el grado: ",ManecillaHoras)
        ManecillaMinutos = (minutos*6) + (segundos*0.1)
        print("La manecilla de minutos está en el grado: ",ManecillaMinutos)
        return abs(ManecillaMinutos-ManecillaHoras)

print(calculaAngulo(3,30,15))