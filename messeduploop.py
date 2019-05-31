#

KICKS=2
TRIES=3
CONVERSIONS=7
kicks=0
tries=0
conversions=0
def main():
    score=int(input('Quanti punti ha fatto? '))

    print(Rugby(score,kicks,tries,conversions))


def Rugby(score,kicks,tries,conversions):
    point=score
    result=[]
    if point>=0 and point>KICKS:
        if(point==0):
            return (kicks,tries,conversions)
        else:
            if point==KICKS:
                kicks=kicks+1
                short=point-KICKS
                Rugby(short,kicks,tries,conversions)
            if point==TRIES:
                tries=tries+1
                short=point-TRIES
                Rugby(short,kicks,tries,conversions)
            if point==CONVERSIONS:
                conversions=conversions+1
                short=point-CONVERSIONS
                Rugby(short,kicks,tries,conversions)
            if (point-KICKS>0):
                short=point-KICKS
                kicks=kicks+1
                Rugby(short,kicks,tries,conversions)
                if kicks*KICKS+tries*TRIES+conversions*CONVERSIONS==score:
                    print(kicks,tries,conversions)
            if (point-TRIES>0):
                short=point-TRIES
                tries=tries+1
                Rugby(short, kicks,tries, conversions)
            if (point-CONVERSIONS>0):
                short=point-conversions
                conversions=conversions+1
                Rugby(short,kicks,tries,conversions)

main()
