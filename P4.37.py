#Decadimento materiali radioattivi
#equazione A=A0*e^(-t*(log(2/h))
#con A la quantità di materiale al tempo t
#A0 la quantità di materiale al tempo 0
#h è il tempo di dimezzamento o emivita

#Tecnezio-99 è un radioisotopo che viene usato nella tomografia
#6 ore tempo di dimezzamento
#A/A0 dopo 24 ore ora dopo ora dopo aver ricevuto la dose A0
from math import log10, exp, log
h=6.0058
A0=0
T=0
LOG=log(2)
A0=float(input("Inserire la quantità di Tecnezio-99 iniziali"))
percent=100
for T in range(0,25,1):
    if A0 == 0:
        break
    if T%6==0:
        A=A0*exp((-T)*LOG/h)
        print(A, "QUANTITÀ DI A")
        percent=A/A0*100
    print("Percentuale ", 100-percent)
    print("Quantità in percentuale ora ", T)
