#trovare tutte le possibili permutazioni del numero di punti fatti da una squadra:
#conversions vale 7
#tries vale 3
#kicks vale 2

CONVERSIONS=7
TRIES=3
KICKS=2

def main():
    numero=input('Qual è stato il punteggio della squadra? ')
    for permutation in Rugby(numero)
        print(permutation)

def Rugby(numero):
    result= []
    
    while(numero>=0):
        if numero%2==0 and numero!=0:
            #Il numero è pari
            #ergo si può sottrarre o tries*2 o conversions*2 o kicks in numero/2*kicks
            #salvo il fatto che ho fatto una di queste operazioni
            
            #si può fare rugby di nuovo numero
        elif numero%2!=0 and numero!=0:
            #Il numero è dispari
            #o gli sottraggo tries o kicks
            
            #rugby di nuovo numero
        #caso base
        elif numero==0:
            return result

