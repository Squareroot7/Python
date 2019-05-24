#Classe amplificatore

class Amplificatore:
    def __init__(self, Type):
        self.Gain=None
        self.R1=None
        self.R2=None
        self.Type=Type
    def getDescription(self):
        print("This is your amplifier %s" % self.Type)
        print("This is your gain %1.3f" % self.Gain)

class Inverter(Amplificatore):
    def __init__(self):
        super().__init__("Inverter")
    def getGain(self, R1, R2):
        self.R1=R1
        self.R2=R2
        self.Gain = -(self.R2/self.R1)
        return self.Gain
class NotInverter(Amplificatore):
    def __init__(self):
        super().__init__("Not Inverter")
    def getGain(self, R1, R2):
        self.R1=R1
        self.R2=R2
        self.Gain = ((self.R2/self.R1)+1)
        return self.Gain
class TensionDivisor(Amplificatore):
    def __init__(self):
        super().__init__("Tension Divider Amplifier")
    def getGain(self, R1, R2):
        self.R1=R1
        self.R2=R2
        self.Gain= (self.R2/(self.R1+self.R2))
        return self.Gain

x=Inverter()
y=NotInverter()
z=TensionDivisor()


while True:
    menu=input("What do you want to analize? ")

    if (menu=="I"):
        R1=int(input("Insert the resistence connected to the signal of the inverter: "))
        R2=int(input("Insert the other one resistence: "))
        x.getGain(R1,R2)
        x.getDescription
        print(x.getGain(R1,R2))
    elif (menu=="N"):
        R1=int(input("Insert the resistance connected to the minus of the amplifier: "))
        R2=int(input("Insert the other one: "))
        y.getGain(R1,R2)
        y.getDescription()
    elif (menu=="T"):
        R1=int(input("Insert the resistance connected to the signal: "))
        R2=int(input("Insert the other one: "))
        z.getGain(R1,R2)
        z.getDescription()
    else:
        break
