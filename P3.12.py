#Programma conversione lettere in voto numerico e viceversa
Scelta=input('Convertitore Voto Numerico/Letterale o Letterale/Numerico inserisci N da numerico a letterale o L da letterale a numerico ')
#int(flag=0)
if Scelta== 'N':
    votoNumerico=(input('Inserisci il voto numerico da convertire '))
    if votoNumerico=="0" or votoNumerico=="0.0":
        print("F")
    str1=(abs(68+49-(ord(votoNumerico[0]))))
    if votoNumerico[2] == "0": 
        print(chr(str1)) #da 52 a 48
    str2=abs(-1+68+49-ord(votoNumerico[0]))
    if votoNumerico[2] == "7" and votoNumerico[0]!="4":
        print(chr(str2),"-")
    str3=abs(-1+69+49-ord(votoNumerico[0]))
    if votoNumerico[2] == "3" and votoNumerico[0]!="0":
        print(chr(str3), "+")

   #if abs(votoNumerico-(float(round(votoNumerico+1))-0.3))<0.00000001
   #     flag=1
   # if abs(votoNumerico-(float(round(votoNumerico))+0.3))<0.00000001
   #     flag=2    
   # if flag==1:
   #     print(chr(69-round(votoNumerico)))+print('-')
   #     flag=0 
   # if flag==2:
   #     print(chr(69-round(votoNumerico)))+print('+')
   #     flag=0

if Scelta== 'L':
    votoLetterale=(input('Inserisci il voto letterale da convertire '))
    if votoLetterale!="A" and votoLetterale!="F":
        if "+" in votoLetterale :
            print(abs(ord(votoLetterale[0])-69-0.3))
        if "-" in votoLetterale :
            print(abs(ord(votoLetterale[0])-69+0.3))
        elif len(votoLetterale)!=2:
            print(abs(ord(votoLetterale[0])-69))
    elif votoLetterale=="F":
        print("0")
