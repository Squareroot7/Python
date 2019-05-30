#trovare tutte le possibili permutazioni del numero di punti fatti da una squadra:
#conversions vale 7
#tries vale 3
#kicks vale 2

kicks=0
tries=0
conversions=0

CONVERSIONS=7
TRIES=3
KICKS=2
case=[]
case.append(KICKS)
case.append(TRIES)
case.append(CONVERSIONS)


def main():
    
    numero=int(input('Qual è stato il punteggio della squadra? '))
    print(Rugby(numero,kicks, tries, conversions))


def Rugby(numero,kicks,tries,conversions,case):
    result=[]
    if numero == 2:
        numero=0
        kicks=kicks+1
        result.append(kicks)
        result.append(tries)
        result.append(conversions)
        return result
    if numero == 3:
        numero=0
        tries=tries+1
        result.append(kicks)
        result.append(tries)
        result.append(conversions)
        return result
    if numero == 7:
        numero=0
        conversions=conversions+1
        result.append(kicks)
        result.append(tries)
        result.append(conversions)
        return result
    else:
        if (numero-KICKS) > 0 or (numero-TRIES)>0 or (numero-CONVERSIONS)>0:
            for i in case[i]
                short=numero-case[i]
                if case[i]==KICKS:
                    kicks=kicks+1
                    short=numero-case[i]
                    Rugby(short,kicks,tries,conversions,case)

                if case[i]==TRIES:
                    tries=tries+1
                    short=numero-case[i]
                    Rugby(short,kicks,tries,conversions,case)

                if case[i]==CONVERSIONS:
                    conversions=conversions+1
                    short=numero-case[i]
                    Rugby(short,kicks,tries,conversions,case)
               
main()
