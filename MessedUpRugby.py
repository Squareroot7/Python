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
    print(Rugby(numero,case,kicks, tries, conversions))


def Rugby(numero,case,kicks,tries, conversions):
    num=numero
    result=[]
    if num>=KICKS:
        if num == KICKS:
            num=0
            kicks=kicks+1
            result.append(kicks)
            result.append(tries)
            result.append(conversions)
        if num == TRIES:
            num=0
            tries=tries+1
            result.append(kicks)
            result.append(tries)
            result.append(conversions)
        if num == CONVERSIONS:
            num=0
            conversions=conversions+1
            result.append(kicks)
            result.append(tries)
            result.append(conversions)
        else:
            if num-CONVERSIONS>0 or num-KICKS>0 or num-TRIES>0:
                for i in range(3):
                    short=num-case[i]
                    if case[i]==KICKS:
                        kicks=kicks+1
                        short=numero-case[i]
                        Rugby(short,case,kicks, tries, conversions)
                        print(kicks,tries, conversions)
                    if case[i]==TRIES:
                        tries=tries+1
                        short=numero-case[i]
                        Rugby(short,case,kicks, tries, conversions)
                        print(kicks, tries, conversions)
                    if case[i]==CONVERSIONS:
                        conversions=conversions+1
                        short=numero-case[i]
                        Rugby(short,case,kicks,tries,conversions)
                        print(kicks,tries,conversions)
    elif num==0:
        return result
main()
