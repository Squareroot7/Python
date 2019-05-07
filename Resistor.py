#Creazione che permetta di catalogare le resistenze in base al loro colore
import string
class Res:
    def __init__(self):
        self._firstband=0
        self._secondband=0
        self._thirdband=0
        self._tolerance=0
    def getValue(self, c1, c2, c3):
        self._firstband=c1*100
        self._secondband=c2*10
        self._thirdband=c3
        return (self._firstband + self._secondband + self._thirdband * (10**(self._thirdband)))

r = Res()
colors={}

#colors = {"nero":"0", "marrone": "1" , "rosso":"2", "arancione":"3", "giallo":"4", "verde":"5", "blu":"6", "viola":"7", "grigio":"8", "bianco": "9"}

#Dizionario
colors["nero"]=0
colors["marrone"]=1
colors["rosso"]=2
colors["arancione"]=3
colors["giallo"]=4
colors["verde"]=5
colors["blu"]=6
colors["viola"]=7
colors["grigio"]=8
colors["bianco"]=9

co1=0
co2=0
co3=0

col1=input("Inserire il primo colore della resistenza ")
co1=colors[col1]
print(col1)
col2 = input("Inserire il secondo colore della resistenza ")
col3 = input("Inserire il terzo colore della resistenza ")

print(col1)
print(co1)
co2=colors[col2]
co3=colors[col3]

print(r.getValue(co1, co2, co3))
