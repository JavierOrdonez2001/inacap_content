

def mayorElemento(par1):

    lista = list(par1)
    mayor = max(lista)
    return mayor

def longitudPalabra(lista):
    palabraCorta = min(lista, key=len)
    palabraLarga = max(lista, key=len)

    return f'palabra corta -> {palabraCorta} // palabra larga -> {palabraLarga}'


def determinacionNotas(lista):

    notaMasAlta = max(lista)
    notaMasBaja = min(lista)
    promedio = (sum(lista)) / len(lista)
    return f'nota mas baja: {notaMasBaja} // nota mas alta {notaMasAlta} // promedio de notas: {promedio}'


def determinacionNumeros(numeros:list):
    promedio = (sum(numeros)) / len(numeros)
    elementoSuperior = []
    elementoInferior = []

    for numero in numeros:
        if numero > promedio:
            elementoSuperior.append(numero)
        if numero < promedio:
            elementoInferior.append(numero)
     
    return f'el promedio es: {promedio} // Los elementos superior al promedio es: {elementoSuperior} // Los elementos inferior al promedio es: {elementoInferior}'



def negativeConvert(lista:list):

    NumNegativeList = []
    for numero in lista:
        numNegative = -1 * numero
        NumNegativeList.append(numNegative)

    return NumNegativeList
        


def imparParOrder(lista:list):
    listaOrdenada = []

    for numero in lista:
        if numero % 2 == 0:
            listaOrdenada.insert(0,numero)
        if numero % 2 == 1:
            listaOrdenada.insert(len(lista),numero)
    
    return f'lista ordenada de par hasta impar: {listaOrdenada}'


def primearUltimapalabra(palabra:str):
    return f'primera letra: {palabra[0]}//ultima letra {palabra[-1]}'


def reverseString(palabra:str):
    palabraAlrevez = ''
    for letra in palabra:
        palabraAlrevez = letra + palabraAlrevez
    
    return palabraAlrevez

def palabraPalindrome(palabra:str):

    palabra
    return

palabra = 'oso'

def P_palindrome(palabra):

    if palabra == palabra[::-1]:

        return 'la palabra es palindrome'
    else:
        return 'la palabra no es palindrome' 


print(P_palindrome(palabra))