
numero= ''
listaNumeros=[]
while numero != 'fin':
    numero= ( input('Inserta un numero:') )
    if numero != '':
        listaNumeros.append(numero)
fichero = open('numeros.txt', 'w')
for numero in listaNumeros:
    if int(numero) % 2 != 0:
        fichero.write(numero+'\n')
fichero.close
