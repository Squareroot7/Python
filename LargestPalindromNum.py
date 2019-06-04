#Largest palindrom number

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#you have to find the LARGEST, so maybe you have to start from the biggest numbers, as 999x999

def main():
    largest=0
    numero= int(input('Inserire un numero '))
    if(Palindroma(numero))!=None:
        print(Palindroma(numero))    

    for i in range(999,100,-1):
        #io non avevo usato i due cicli ma usando i*(i-1) avevo fatto le combinazioni più alte ed era uscito. stampava se il risultato era palindromo 
        for j in range(999,100,-1):
            num1=i*j
            if Palindroma(num1) != None:
                if(num1>largest):
                    largest=num1
                if(num1<largest):
                    break
    print(largest)

        #if num1!=None and num2!=None:
        #    if num1>num2:
        #        print("This is the largest prime number %d" %num1 ) 
        #        break 
        #    else: 
        #        print("This is the largest prime number %d" %num2 ) 
        #        break 


def Palindroma(numero):
    num=str(numero)
    lenght=len(num)
    first = num[0]
    last= num[lenght-1]
    if lenght%2==0:
        for i in range(round(lenght/2)):
            if num[i]==num[lenght-1-i] and (i+1==lenght-1-i):
                return num
            #elif i+1==lenght-1-i:
            #    print('Il numero non è palindromo')
    else:
        for i in range(round((lenght-1)/2)):
            if num[i]==num[lenght-1-i] and i+2==(lenght-1-i):
                return num
            #elif i+2==lenght-1-i:
            #    print('Il numero non è palindromo')


main()
