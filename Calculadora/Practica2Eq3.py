#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Nodo:

    def __init__(self, data):

        self.izq = None
        self.der = None
        self.data = data

def isEmpty(arr):
    if not arr: 
        return True
    else: 
        return False
    
def estaBalanceado(str): # listo, pero no checado
    abiertos = ["("] 
    cerrados = [")"] 
    pila = []
    j = 0
    
    for i in str: 
        if i in abiertos: 
            pila.append(i) 
            j = j + 1
        elif i in cerrados: 
            if(j > 0): #si empiez con un parentesis cerrado no hago comparación y lo meto a la pila
                if(abiertos.index(pila[j-1]) == cerrados.index(i)):
                    pila.pop(j-1)
                    j = j - 1
                else:
                    pila.append(i)
                    j = j + 1
            else:
                pila.append(i)
                j = j + 1
    
    if(len(pila) == 0):
        return True
    else:
        return False

def esOperador(char): # listo
    if '+' == char or '-' == char or '/' == char or '^' == char or '*' == char:
        return True
    else:
        return False
    
def NoEsOperadorNeg(char):
    if char == '-':
        return False
    else:
        return True

def esParentesis(char): # listo
    if '(' == char:
        return -1
    elif ')' == char:
        return 1
    else:
        return 0
    
def esNumero_o_Punto(num): # listo
    aceptados = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']    
    if num in aceptados:
        return True
    else:
        return False
    
def sinParenOperaJuntos(str):   
        i = 0
        ant='#'
        resp = True        
        while( (i < len(str)) and resp):
            act=str[i]
            if(act != '-'):
                b1= not(esOperador(ant) and esOperador(act))
            elif act == '-':
                b1= not(esOperador(ant) and NoEsOperadorNeg(act))
            b2= not( (ant =='(') and (act==')'))
            b3= not( (ant =='(') and (act==')'))
            b4= not( (ant =='(') and esOperador(act))
            resp= b1 and b2 and b3 and b4
            ant=act
            i = i +1
        return resp

def checarOperaYNumer (str):  #checa qye no hay más operadores que números en una expresión
    i = 0
    num = 0  #contador de numeros
    op = 0   #contador de operadores
    ant='#'       
    while( (i < len(str))):
        act = str[i]
        if(esNumero_o_Punto(act) and not esNumero_o_Punto(ant)): #por si es un numero de varios digitos, etnonces no sumarlo
            num = num + 1
        elif (esOperador(act) and not esOperador(ant)):  #si es un numero negativo no contarlo
            op = op + 1
        ant = act
        i = i + 1
    if num > op:
        return True
    else:
        return False   

def soloParen (str): #checa que no usemos [, ], {, } 
    parent = ['[',']','{','}']
    i = 0
    resp = True        
    while( (i < len(str)) and resp):
        act=str[i]
        if(act in parent):
            resp = False
        else:
            i = i +1
    if(resp == True):
        return True
    else:
        return False
   
def noLetras (str):   #checar que no hay letras
    i = 0
    resp = True
    while (i < len(str) and resp):
        act = str[i]
        if(act.isalpha()): #es letra
            resp = False
        i = i + 1
    if(resp == True):
        return True
    else:
        return False 

    
def tokeniza(str): # listo
    arr = []
    i = 0
    strB = str.replace(" ", "")  #quita espacios vacios
    while(i < len(strB)): # traversa el string
        token = strB[i]
        restoDelString = strB[i+1:]
        if esNumero_o_Punto(token): # podemos tener numeros de: 1 digito, + de 1 digito, decimales
            num = token
            for j in restoDelString: # recorremos el resto del string buscando que los siguientes objetos sean numeros o puntos continuos
                if not esNumero_o_Punto(j):
                    break # cuando encontremos algo que no sea numero salimos del for 
                else:
                    num = num + j # de otra forma lo agregamos al token
                    i = i + 1
            arr.append(num)
            i = i + 1  
        elif NoEsOperadorNeg(token): #si es true, entonces no es el operador -
            arr.append(token) # porque solo tenemos operadores de 1 simbolo
            i = i + 1
        elif  NoEsOperadorNeg(token) == False: #es el operador -
            if(esOperador(strB[i-1]) or esParentesis(strB[i-1]) == -1): 
            #si el token anterior  es operando o (, entonces el negativo es parte del número
                num = token
                for j in restoDelString: # recorremos el resto del string buscando que los siguientes objetos sean numeros o puntos continuos
                    if not esNumero_o_Punto(j):
                        break # cuando encontremos algo que no sea numero salimos del for 
                    else:
                        num = num + j # de otra forma lo agregamos al token
                        i = i + 1
                arr.append(num)
                i = i + 1
            else:
             #si el token anterior no es operando o (, entonces el negativo es parte del número
                arr.append(token) # porque solo tenemos operadores de 1 simbolo
                i = i + 1
        elif esParentesis(token) != 0:
            arr.append(token)
            i = i + 1
    return arr

       
def revisaSintaxis(string):
    if string == None: # checa si el string es vacio
        return False
    if not type(string) == str: # checa si el tipo de la variable es un string
        return False
    if string == '':
        return False
    if not noLetras(string):
        return False
    if not estaBalanceado(string): # checa si la expresion tiene parentesis balanceados
        return False
    if not sinParenOperaJuntos(string): #que no tenga dos parentesis juntos
        return False
    if not checarOperaYNumer(string):  #hay más operadores que números
        return False
    if not soloParen(string):  #solo uses '(' y ')' en las expresiones
        return False
    
    return True


def comparaPrioridad(op1, op2): #regresa true si op1 tiene mayor prioridad que op2
    maxPri = ['^']
    secPri = ['*','/']
    terPri = ['+','-']
    if op1 in maxPri:
        return True
    elif op1 in secPri:
        if op2 in maxPri:
            return False
        else:
            return True
    else:
        if op2 in terPri:
            return True
        else:
            return False
            
def postOrden(nodo):
    pila = [] 
    if nodo:
        pila.extend(postOrden(nodo.izq))# recorre izq
        pila.extend(postOrden(nodo.der))# recorre der
        pila.append(nodo.data)# visita
    return pila   
            
def evaluaOperador(num1, op, num2):
    if op == '+': return num1 + num2
    if op == '^': return num1 ** num2
    if op == '-': return num1 - num2
    if op == '/': return num1 / num2
    if op == '*': return num1 * num2

def evaluaPostfix(arr):
    pila1 = []
    i = 0
    while i < len(arr):
        if esNumero_o_Punto(arr[i][-1]):  #checamos el último digito por si es -3 que si lo tome como número
            pila1.append(float(arr[i]))
        else:
            t = pila1.pop()
            s = pila1.pop()
            res = evaluaOperador(s, arr[i], t)
            pila1.append(res)
        i = i + 1
    return pila1.pop()

def evaluaArbol(lista):
    a=postOrden(lista.pop())
    return a

def creaArbol(arr):
    pilaA = [] # pila de operadores
    pilaB = [] # pila de arboles
    for i in arr: 
        if esNumero_o_Punto(i[-1]): # si es operando
            arbol = Nodo(i) 
            pilaB.append(arbol) 
        elif esParentesis(i) == -1: # si es ( se agrega el token a la pila A
            pilaA.append(i)
        elif esParentesis(i) == 1: # si es )
            while(esParentesis(pilaA[-1]) != -1):  
            #al solo haber operadores o parentesis si no es parentesis entonces se saca de B
                a = pilaA.pop()  #se saca el elemento de la pila A
                P = pilaB.pop()
                S = pilaB.pop()
                arbol2 = Nodo(a)
                arbol2.der = P
                arbol2.izq = S
                pilaB.append(arbol2)
            pilaA.pop() #elimina el parentesis izquierdo
        else:
            
            while not isEmpty(pilaA) and esParentesis(pilaA[-1]) != -1 and comparaPrioridad(pilaA[-1],i) == True:
                a = pilaA.pop()  #se saca el elemento de la pila A
                P = pilaB.pop()
                S = pilaB.pop()
                arbol3 = Nodo(a)
                arbol3.der = P
                arbol3.izq = S
                pilaB.append(arbol3)
            pilaA.append(i)

    while not isEmpty(pilaA):
        arbolUtopico = Nodo(pilaA.pop())
        arbolUtopico.der = pilaB.pop()
        arbolUtopico.izq = pilaB.pop()
        pilaB.append(arbolUtopico)
        
    return pilaB

def calculadora(string): 
    if(string != None):
        if(type(string) == str):
            print ("La expresión es: " + string)
    if not revisaSintaxis(string): # paso 1 - revisamos la validez sintactica
        return 'la expresion es incorrecta'
    arr = tokeniza(string)  #parte el string en tokens atomicos
    res = creaArbol(arr)
    post = evaluaArbol(res)
    return evaluaPostfix(post)


#correctos
str0 = '33-33'
str1 = '21+1'
str2 = '1+1'
str3 = '(1+2)*43'
str4 = '(2*(2+4)+3)'
str5 = '2^3' 
str6 = '2.2+2'
str7 = '2+-3'
str8 = '.02 + 213' 
str9 = '55*-3'
str10 = '(2+-3)-8'
str11 = '45'
str12 = '(2-6)*3+5'
str13 = '2-6*3+5'
str14 = '2-6+3-5'
str15 = '(4/2)'
str16 = '((2+17))'
#incorrectos
str20 = '(1+1))'
str21 = '(1++1)'
str22 = '(^(2^3))'
str23 = None
str24 = '()'
str25 = '1+2+'
str26 = '*'
str27 = 'h1h2'
str28 = ''
str29 = '2**3'
str30 = '[2+2]'
str31 = 2


print ("\n")
print ("CORRECTOS")
print ("Resultado: " + str(calculadora(str0)))
print ("Resultado: " + str(calculadora(str1)))
print ("Resultado: " + str(calculadora(str2)))
print ("Resultado: " + str(calculadora(str3)))
print ("Resultado: " + str(calculadora(str4)))
print ("Resultado: " + str(calculadora(str5)))
print ("Resultado: " + str(calculadora(str6)))
print ("Resultado: " + str(calculadora(str7)))
print ("Resultado: " + str(calculadora(str8)))
print ("Resultado: " + str(calculadora(str9)))
print ("Resultado: " + str(calculadora(str10)))
print ("Resultado: " + str(calculadora(str11)))
print ("Resultado: " + str(calculadora(str12)))
print ("Resultado: " + str(calculadora(str13)))
print ("Resultado: " + str(calculadora(str14)))
print ("Resultado: " + str(calculadora(str15)))
print ("Resultado: " + str(calculadora(str16)))

print ("\n")
print("INCORRECTOS")
print ("Resultado: " + str(calculadora(str20)))
print ("Resultado: " + str(calculadora(str21)))
print ("Resultado: " + str(calculadora(str22)))
print ("Resultado: " + str(calculadora(str23)))
print ("Resultado: " + str(calculadora(str24)))
print ("Resultado: " + str(calculadora(str25)))
print ("Resultado: " + str(calculadora(str26)))
print ("Resultado: " + str(calculadora(str27)))
print ("Resultado: " + str(calculadora(str28)))
print ("Resultado: " + str(calculadora(str29)))
print ("Resultado: " + str(calculadora(str30)))
print ("Resultado: " + str(calculadora(str31)))


