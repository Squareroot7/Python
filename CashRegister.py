#Creazione di un programma di interfaccia di cassa

class CashRegister:
    def __init__ (self):
        self._itemCount=0
        self._totalPrice=0
        self._discount=80/100
    def addItem(self, price):
        #Dall'interno del corpo di un metodo si ha accesso alle variabili di esemplare dell'oggetto su cui si agisce
        self._itemCount=self._itemCount + 1
        self._totalPrice=self._totalPrice + price
    def getTotal(self):
        return self._totalPrice
    def getTotalSales(self):
        return self._totalPrice*self._discount
    def getCount(self):
        return self._itemCount
    def clear(self):
        self._itemCount=0
        self._totalPrice=0

register=CashRegister()

print("Benvenuto alla cassa fai da te")

while(1):
    prod=input("Scannerizzare il prossimo prodotto, premi qualsiasi tasto, premi t per totale, e per uscire ")
    if prod=="e":
        print("Arrivederci e grazie per aver usato cassa fai da te ")
        break
    if prod=="t":
        print(register.getTotal(), " Totale da pagare ")
        print(register.getCount(), " Numero di prodotti acquistati")
        print(register.getTotalSales(), "Se ha la carta clienti con lo sconto del 20% pagherà")
    else:
        try:
        value=float(input("Scannerizzare il codice a barre del prodotto (inserire prezzo) "))
        register.addItem(value)

