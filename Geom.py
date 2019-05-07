#Programma per l'elaborazione di elementi di geometria e algebra lineare


#è importante definire l'elemento matrice e i numeri frazionali (in teoria definiti in altri moduli)

#operazioni base
import matrici.py

class Vector:
    def __init__(self,coordx, coordy, coordz):
        self._coordx
        self._coordy
        self._coordz
        self._direzione=0
        self._verso=1
    def Modulo(self):
        #Il modulo si definisce facendo il modulo delle coordinate rad (ax-bx)quadr same per y
        return ((self._coordx**2+self._coordy**2+self._coordz**2)**(1/2))
    def ModuloScalare(self, scalare):
#        boh
    def SumVectorscalar(self, v1):
        return self._coordx*v1._coordx + self._coordy*v1._coordy+self._coordz*v1._coordz
    def ProdottoVettoriale(self,altro): #Regola del parallelogramma usabile solo con FindAngle
#        Regoladelparallelogramma
        x=self._coordy*altro._coordz-altro._coordy*self._coordz
        y=self._coordx*altro._coordz-altro._coordx*self._coordz
        z=self._coordx*altro._coordy-altro._coordx*self._coordy
        return Vector(x,y,z)
    def ProdottoScalare
    def FindAngle(self):
        arccos(prodscalare su i moduli)
    def VolumeParallelepipedo(self,w,v)
        volume=somma delle x, y z de prodotto vettoriale

