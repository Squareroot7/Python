#Programma per la creazione della classe Matrici
from itertools import product
class Matrix:
    def __init__(self, r, c, n):
        if r==0 or c==0:
            raise ZeroRowORColumn("Matrix cannot have 0 rows or 0 columns")
        else:
            self.righe= [[n]*(c) for i in range(r)]
            self.colonne=c
            self.r=r
            self.values=[]
            self.n=n #Valori inizializzazione matrice
    def MatrixDimension(self):
        Dim=self._righe*self._colonne
        return Dim
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
    def prodMatrix(self,num):
        self.n=self.n*num
        self.righe=[[self.n]*(self.colonne) for i in range(self.r)]
    def InsertValue(self, r, c, value):
        for i in range(self.r):
            for j in range(self.colonne):
                if (i==r and j==c):
                    self.righe[i]=value*

        

myMat=Matrix(4,5,0)
print(str(myMat.righe))
print(str(myMat.colonne))
myMat.prodMatrix(2)
print(str(myMat.righe))
myMat.InsertValue(0,0,10)
print(str(myMat.righe))
