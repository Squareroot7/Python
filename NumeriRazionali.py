#Classe frazione, fatta da un numeratore e un denominatore.
#Modello per un numero razionale.
#Vogliamo usare i numeri in frazione come usiamo gli interi o in virgola mobile

class Fraction:             #da cosa è fatta una frazione? Numeratore e Denominatore.
    def __init__(self, numerator, denominator) #Numeratore e denominatore sono immutabili quindi vanno passati
        self._numerator=0   #visualizzeremo il segno solo sul numeratore
        self._denominator=1 #scegliamo di tenere il denominatore sempre positivo
                            #rappresenteremo il numero sempre in forma ridotta
        if denominator == 0 :
            raise ZeroDivisionError("Denominator cannot be zero.")
        if numerator == 0 :
            self._numerator=0   #visualizzeremo il segno solo sul numeratore
            self._denominator=1 #scegliamo di tenere il denominatore sempre positivo
        else :
            if(numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0): #NUMERI NEGATIVI 
                sign= -1
            else: #NUMERI POSITIVI
                sign= 1
            #algoritmo di riduzione ai minimi termini
            a=abs(numerator)
            b=abs(denominator)
            while a % b != 0 :
                tempA=a
                tempB=b
                a=tempB
                b=tempA%tempB
            self._numerator= abs(numerator) // (b*sign)
            self._denominator= abs(denominator) // b
