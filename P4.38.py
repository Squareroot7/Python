# La formula che caratterizza il rapporto spire è Ps=(n*Vs)/(n^2*R0 + Rs)
# Vogliamo trovare il massimo rapporto che rende massima la potenza trasferita dall'altoparlante
#da 0,01 a 2 con passo 0,01

#R0=20 ohm
#Vs=40 V
#Rs=8 ohm

Rs=8
Vs=40
R0=20
Ps=0
PsPrevious=0;
largest=0

for n in range(1 , 200, 1):
    N=n*0.01
    PsPrevious=Ps
    Ps=(N*Vs)/(N**2*R0 + Rs)
    print(Ps, "Potenza")
    #print(N , "Valore di N attuale")
    if Ps > largest:
        largest=Ps
        Nlargest=N
        print(Nlargest, "Valore N")
        print(largest, "Valore di potenza maggiore")
print(Nlargest, "Valore N finale")
print(largest, "Valore di potenza maggiore finale")
