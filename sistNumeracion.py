import unittest

def decimal2binario(number):

    result = ''
    aux = ''

    if number == 0:

        return 0
    while number > 0:

        result += str(number%2)
        number //= 2

    result += str(number)

    for i in range(len(result)-1,-1,-1):
        
        aux += result[i] 
    return aux

def binario2decimal(number):

    result = 0
    j = 0

    for i in range(len(number)-1,-1,-1):
        
        result += int(number[i])* (2**j)
        j += 1
    return result
    
def decimal2octal(number):

    result = ''
    aux = ''

    if number == 0:

        return 0
    while number >= 8:

        result += str(number%8)
        number //= 8

    result += str(number)

    for i in range(len(result)-1,-1,-1):
        
        aux += result[i] 
    return aux

def octal2decimal(number):

    result = 0
    j = 0

    for i in range(len(number)-1,-1,-1):
        
        result += int(number[i])* (8**j)
        j += 1
    return result

def decimal2hexa(number):

    result = ''
    aux = ''

    if number == 0:

        return 0
    while number > 16:

        aux2 = str(number%16)
        
        result += swich(aux2)
        number //= 16

    result += str(swich(str(number)))

    for i in range(len(result)-1,-1,-1):
        
        aux += result[i] 
    return aux

def swich(aux2):
    if aux2 == '10':
           aux2 = 'A'
    elif aux2 == '11':
           aux2 = 'B'
    elif aux2 == '12':
           aux2 = 'C'
    elif aux2 == '13':
           aux2 = 'D'
    elif aux2 == '14':
           aux2 = 'E'
    elif aux2 == '15':
           aux2 = 'F'
    return aux2

def hexa2decimal(number):

    result = 0
    j = 0

    for i in range(len(number)-1,-1,-1):
        aux = str(number[i])
        if aux == 'A':
           aux = 10
        elif aux == 'B':
           aux = 11
        elif aux == 'C':
           aux = 12
        elif aux == 'D':
           aux = 13
        elif aux == 'E':
           aux = 14
        elif aux == 'F':
           aux = 15
        result += (int(aux) * (16**j))
        j += 1
    return result

def binario2octal(number):

    aux = binario2decimal(number)
    result = int(decimal2octal(aux))
    return result

def binario2hexa(number):
    aux = binario2decimal(number)
    print(aux)
    result = int(decimal2hexa(aux))
    return result