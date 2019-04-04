#Progetto per modifica automatica di Teamware Phonebook
#Il programma deve, ricevere un nome, il rispettivo numero da modificare, cercarlo, sostituirlo al posto giusto, e chiedere il nome successivo fino a che non viene premuto un tasto di uscita.
#Interessante l'implementazione per l'inserimento corretto di un nuovo nome.


ind=open('/home/squareroot/teamware-phonebook/index.html','r+')
nome=input('Inserire il nome da modificare in maiuscolo ')

import string
import fileinput
def sovrascrittura(a,b):
    f=open('/home/squareroot/Desktop//teamware-phonebook/index.html','r')
    filedata=f.read()
    f.close()
    newdata= filedata.replace(a, b)
    f=open('/home/squareroot/Desktop/teamware-phonebook/index.html','w')
    f.write(newdata)
    f.close()

while nome !='E':
    #cercare la riga del nome nel file index da modificare
    #vai alla riga dopo e rimpiazza il numero che inizia per 2       
    #modificare il numero nel file index passando alla riga dopo del file 
    #chiedere il nome successivo
    line=ind.readline()
    while line != "":
        if line.find(nome) != -1:       #Cerca il nome nella riga che sto leggendo se lo trova entra nell'if
            azione=input("Inserisci N per modificare il nome e P per il numero postazione E per uscire ")
            if azione=="E":
                break
            if azione=="N":
                #DA QUI INIZIA L'ALGORITMO DELLA MODIFICA DEL NOME
                posizione=line.find(nome)+1
                nuovoNome=input("Inserisci il nuovo nome da sostituire in maiuscolo ")
                #Procedura di sovrascrittura
                sovrascrittura(nome, nuovoNome)
            if azione=="P":
                #DA QUI INIZIA L'ALGORITMO DELLA MODIFICA DEL NUMERO
                line=ind.readline()         #Se lo trova salta alla riga successiva in cui c'è il numero della postazione
                i=0                         #indice i per trovare il primo carattere numerico, che sarà il numero di postazione
                while not line[i].isdigit():
                    i=i+1
                numero=input('Inserire il numero nuovo ')   #Faccio inserire il numero da sostituire
                numeroPrima=line[i:i+3]                     #Il numero precedente lo salvo per usarlo nel replace, che va dall'indice del primo carattere numerico a +3
                #Procedura di sovrascrittura
                sovrascrittura(numeroPrima,numero)
        line=ind.readline()             #Salto alla riga successiva se non ho trovato il nome nella riga prima
    ind.close()                         #Chiudo il file
    nome=input('Inserire il nome da modificare in maiuscolo ')
    ind=open('/home/squareroot/Desktop/teamware-phonebook/index.html','r+')
print('Procedura completata')
