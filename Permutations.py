#Creare un programma che gestisca le permutazioni di una stringa

#Prendo in carico una stringa
parola=input('Inserisci la stringa di cui fare la permutazione: ')
def main():
    for i in Permutazione(parola):
        print(i)

def Permutazione(parola):
    result= []

    if len(parola)==0:
        result.append(parola)
        return result
    else:
        for i in range(len(parola)):
            short=parola[:i]+ parola[i+1:] #dall'inizio a i escluso da i+1 alla fine
            shorterPermutation= Permutazione(short)
            for string in shorterPermutation:
                result.append(string+parola[i])
        return result
main()
