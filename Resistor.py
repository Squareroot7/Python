#Creazione che permetta di catalogare le resistenze in base al loro colore

#Codice 4 anelli

class Res:
    def __init__(self):
        self._firstband=0
        self._secondband=0
        self._thirdband=0
        self._tolerance=0
    def getValue(self, c1, c2, c3):
        self._firstband=c1*10
        self._secondband=c2
        self._thirdband=c3
        return ((self._firstband + self._secondband) * (10**(self._thirdband)))

r = Res()

#Dizionario
colors = {"nero":0, "marrone": 1 , "rosso":2, "arancione":3, "giallo":4, "verde":5, "blu":6, "viola":7, "grigio":8, "bianco": 9}

co1=0
co2=0
co3=0

col1=str(input("Inserire il primo colore della resistenza "))
co1=int(colors[col1])
print(co1)
col2 = input("Inserire il secondo colore della resistenza ")
co2=int(colors[col2])
print(co2)
col3 = input("Inserire il terzo colore della resistenza ")
co3=int(colors[col3])
print(co3)

print(r.getValue(co1, co2, co3))
