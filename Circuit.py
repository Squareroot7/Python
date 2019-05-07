#Questo programma ha l'obiettivo di rappresentare  un circuito elettrico costituito da una configurazione arbitraria di resistori, usando la legge di ohm per calcolare la resistenza complessiva
#Circuit con il metodo getResistance, poi sottoclasse resistor i cui singoli oggetti siano resistori con sottoclasse Parallel e Serial ciarscuna delle quali contiene una lista di oggetti di tipo circuit

class Circuit():
    def __init__(self, typ):
        self._type=typ
        self._value=0
    def GetResistance(self, val):
        self._value=val
    def PrintValue(self):
        print(self._value)
class Resistor(Circuit):
    def __init__(self):
        super().__init__("R")
    #def GetResistance(self, val):
    #    return self._value=val
    def Parallel(self, Res2value):
            self._value=((1/(self._value)+1/(Res2value._value)))**(-1)
            return self._value
    def Serial(self,Res2value):
            return (self._value+Res2value._value)
#class Capacitor(Circuit):

R1=Resistor()
R1.GetResistance(6)
R1.PrintValue()
R2= Resistor()
R2.GetResistance(4)
R1.Serial(R2)
R1.PrintValue()

