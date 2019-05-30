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
def main():
    
    numero=int(input('Qual è stato il punteggio della squadra? '))
    print(Rugby(numero,kicks, tries, conversions))

 #   for result in Rugby(numero,kicks, tries, conversions):
  #      print(result)


def Rugby(numero,kicks,tries,conversions):
    resulti=[]
    result=[resulti]
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
    elif numero!=0:
        if (numero-KICKS) > 0 or (numero-TRIES)>0 or (numero-CONVERSIONS)>0:
                short=numero-KICKS
                kicks=kicks+1
                shorter=(Rugby(short,kicks,tries,conversions))
                resulti.append(shorter)
                short=numero-TRIES
                tries=tries+1
                shorter=(Rugby(short,kicks, tries, conversions))
                resulti.append(shorter)
                short=numero-CONVERSIONS
                conversions=conversions+1
                shorter=(Rugby(short,kicks, tries, conversions))
                resulti.append(shorter)
main()
