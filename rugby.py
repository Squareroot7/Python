
def main():
    score=int(input('Inserisci il punteggio: '))
    Rugby(score)

def Rugby(score):
    KICKS=2
    TRIES=3
    CONVERSIONS=7

    for i in range(round((score+1)/2)): #Considering the max number 222 I assured that the rounding would provide the correct maximum number
        for j in range(round((score+1)/3)):
            for k in range(round((score+1)/7)): #potrei eliminare il terzo ciclo e vedere se il risultato è divisibile per 7
                if ((2*i + 3*j + 7*k) == score):
                    print(k,j,i)
main()
