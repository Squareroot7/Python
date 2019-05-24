#Classe frazione, fatta da un numeratore e un denominatore.
#Modello per un numero razionale.
#Vogliamo usare i numeri in frazione come usiamo gli interi o in virgola mobile
 
class Fraction:             #da cosa è fatta una frazione? Numeratore e Denominatore.
    def __init__(self, numerator=0, denominator=1): #Numeratore e denominatore sono immutabili quindi vanno passati
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
            #Algoritmo di riduzione ai minimi termini
            a=abs(numerator)
            b=abs(denominator)
            while a % b != 0 :
                tempA=a
                tempB=b
                a=tempB
                b=tempA%tempB
            self._numerator= abs(numerator) // (b*sign)
            self._denominator= abs(denominator) // b
    def __add__(self, numadd): 
        num=(self._numerator * numadd._denominator + self._denominator * numadd._numerator)        
        den=(self._denominator*numadd._denominator)
        return Fraction(num,den)
    def __sub__(self, numsub):
        num=(self.numerator * numsub._denominator - self._denominator * numsub._numerator)
        den=(self._denominator*numsub._denominator)
        return Fraction(num,den)
    def __mul__(self, nummul):
        num=(self._numerator * nummul._numerator)
        den=(self._denominator * nummul._denominator)
        return Fraction(num,den)
    def __truediv__(self, numdiv):
        num=(self._numerator * numdiv._denominator)
        den=(self._denominator * numdiv._numerator)
        return Fraction(num,den)
    def __neg__(self):
        num=(self._numerator * -1)
        den=(self._denominator)
        return Fraction(num,den)
    def __eq__(self, numb):
        return (self._numerator==numb._numerator and self._denominator==numb._denominator)
    def __lt__(self, numb):
        return (self._numerator * numb._denominator < self._denominator * numb._denominator)
    def __repr__(self):
        return str(self._numerator) + "/" + str(self._denominator)
    def __flo__(self):
        return self._numerator / self.denominator
num=0
den=0
#Calcolatrice

#Menù calcolatrice di numeri razionali

menu=input("Inserisci A per somma, S per sottrazione, M per moltiplicazione, D per divisione")
while(menu !="E" and menu !="e"):
    if(menu=="A" or menu=="a"): 
        
        n1 , d1 =(input("Inserisci la frazione: ").split('/'))
        int(n1)
        int(d1)
        #n1=int(input("Inserisci numeratore del primo numero "))
        #d1=int(input("Inserisci il denominatore del primo numero"))
        
        frac1=Fraction(n1,d1)
        n2=int(input("Inserisci numeratore del secondo numero "))
        d2=int(input("Inserisci il denominatore del secondo numero"))
        frac2=Fraction(n2,d2)
        fracSum=frac1+frac2
        print(fracSum)
        menu=input("Inserisci A per somma, S per sottrazione, M per moltiplicazione, D per divisione")
    elif(menu=="S" or menu=="s"):
        n1=int(input("Inserisci numeratore del primo numero "))
        d1=int(input("Inserisci il denominatore del primo numero"))
        frac1=Fraction(n1,d1)
        n2=int(input("Inserisci numeratore del secondo numero "))
        d2=int(input("Inserisci il denominatore del secondo numero"))
        frac2=Fraction(n2,d2)
        fracSub=frac1-frac2
        print(fracSub)
        menu=input("Inserisci A per somma, S per sottrazione, M per moltiplicazione, D per divisione")
    elif(menu=="M" or menu=="m"):
        n1=int(input("Inserisci numeratore del primo numero "))
        d1=int(input("Inserisci il denominatore del primo numero"))
        frac1=Fraction(n1,d1)
        n2=int(input("Inserisci numeratore del secondo numero "))
        d2=int(input("Inserisci il denominatore del secondo numero"))
        frac2=Fraction(n2,d2)
        fracMul=frac1*frac2
        print(fracMul)
        menu=input("Inserisci A per somma, S per sottrazione, M per moltiplicazione, D per divisione")
    elif(menu=="D" or menu=="d"):
        n1=int(input("Inserisci numeratore del primo numero "))
        d1=int(input("Inserisci il denominatore del primo numero"))
        frac1=Fraction(n1,d1)
        n2=int(input("Inserisci numeratore del secondo numero "))
        d2=int(input("Inserisci il denominatore del secondo numero"))
        frac2=Fraction(n2,d2)
        fracDiv=frac1/frac2
        print(fracDiv)
        menu=input("Inserisci A per somma, S per sottrazione, M per moltiplicazione, D per divisione")
