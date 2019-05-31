
def main():
    score=int(input('Inserisci il punteggio: '))
    Rugby(score)

def Rugby(score):
    KICKS=2
    TRIES=3
    CONVERSIONS=7
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if ((2*i + 3*j + 7*k) == score):
                    print(k,j,i)
main()
