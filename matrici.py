#Programma per la creazione della classe Matrici
from itertools import product
class Matrix:
class Matrix:
    def __init__(self, r, c)
        self._righe
        self._colonne
    def MatrixDimension(self)
        Dim=self._righe*self._colonne
        return Dim
    def __init__(self, r, c):
        if r==0 or c==0:
            raise ZeroRowORColumn("Matrix cannot have 0 rows or 0 columns")
        else:
            self.righe= [[0]*c for i in range(r)]
            self.colonne=c
    def __setitem__(self, idx, item):
        self.righe[idx]=item
    def __getitem__(self, idx):
        return self.righe[idx]
    def getRank(self):
        return (self.righe, self.colonne)
    def __repr__(self):
        s=str(self.righe)
        rank=str(self.getRank())
        rep="Matrix: \"%s\",rank:\"%s\"" %(s,rank)
        return rep

myMat=Matrix(2,2)


