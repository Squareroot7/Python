#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
divisor=20


def SmallestDivisible(divisor):
    smallest=1
    #Numeri primi
    prime=[]
    for i in range(divisor+1):
        if i==2:
            prime.append(i)
        if Prime(i)!=None:
            prime.append(i)
            print(prime)
    #Esponente massimo
    for j in range(divisor):
        if divisor> 2**j:
            exp=j
        else:
            break
    #Moltiplico prima i quadrati perfetti massimi, passo tutti i primi e li elevo al massimo esponente
    for i in range(divisor+1,1,-1):
        for p in prime:
            for j in range(exp+2,1,-1):
                if p**j==i and smallest%p!=0:
                    print(j)
                    smallest=smallest*(p**(j-1))
                    print(p**(j-1), 'is the max prime')
                    print(smallest, 'is the smallest')


#se un numero è uguale ad uno dei numeri primi elevato ad un numero intero, come 16 o 8 o 9, quello con l'esponente maggiore va preso,
    #quindi smallest=smallest per esponente-1 perchè uno è già stato moltiplicato
    #massimo esponente if divisore >2**j salva j
    #prime**range(j) ==i moltiplica per prime**(j-1)
    for p in prime:
        smallest=smallest*p
    return smallest        

    
def main():
    divisor=int(input('I want a number divisible for all the number from 1 to: '))
    print(SmallestDivisible(divisor))

#Funzione che verifica che un numero sia primo
def Prime(num):
    #find a the prime number
    for i in range(num):
        if i!=0 and i!=1:
            if num % i == 0:
                return None
            elif num % i != 0:
                if i==(num-1):
                    return num

main()
