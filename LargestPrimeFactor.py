#Largest prime factor

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
def main():

#assolutamente non ottimizzato, pessimo per i numeri grandi come 600....
    lista=[]
    maxnumber=int(input("Inserire il numero"))
    for divisore in range(maxnumber):
        if divisore!=0 and maxnumber % divisore == 0:
            prime=Prime(divisore)
            if prime!=None:
                lista.append(divisore)

    print(lista)
    print(max(lista))
    


''' Tentativo inutile di trovare un po' di numeri primi e poi trovare il più grande
    bigprime=0
    maxnumber=int(input("Inserire il numero "))
    listanprimi=[]
    divisorimax=[]
    for i in range(1000):
        value=Prime(i)
        if value!=None:
            listanprimi.append(value)
    #print(listanprimi)
    for r in listanprimi:
        if maxnumber % r==0:
            divisorimax.append(r)
    print(divisorimax)
    print(max(divisorimax))
'''
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

''' trovato su internet non funziona con i quadrati perfetti
n =100 # 600851475143
i = 2
while i * i <= n:
    while n % i == 0:
        n = n / i
        round(n)
    i = i + 1
print(n)
'''
