# Esto seria un comentario
print('Hola mundo') # Esto es otro comentario

# RAM: Cuaderno de cuadricula donde escribo cosas
# Al lado de algo que yo escribo en mi cuaderno (RAM) pongo un postit <- Variable
# Variables: Apuntador | Marcador a algo que tengo en la memoria RAM
a=5
    # 1º Escrito en la RAM el número 5
    # 2º Crear una variable (POSTIT con texto escrito 'a')
    # 3º Pega el positit al lado del 5 
print(a)
a='texto'
print(a)

# Definimos variables de distintos tipos
mi_numero=7
mi_texto='mi texto'
mi_gran_texto="""
Escribir un texto que ocupe
varias lineas

tantas como yo quiera
"""

# Establecer comentarios de multiples lineas
"""
mi_logica=True
mi_logica=False
"""

# Operadores básicos aritmeticos -> NUMERO
3+5-1*7/4
5/2  # 2.5 
5//2 # 2 <- Division entera
5%2  # 1 <- Resto
# Operadores relacionales -> VALOR LOGICO: TRUE o FALSE
1==1
1!=2
1<4
4>=2
# Operadores logicos -> VALOR LOGICO: TRUE o FALSE
1==1 and 2<4   # TRUE
1==1 or 2<4    # TRUE
not 1==1       # FALSE

print(mi_gran_texto)

"""// JAVA, C, C++, C#
/*
    Todo lo que ponga aqui seria un comentario en java
    aunque ocupe varias lineas
*/
<!-- comentario -->
"""

# FUNCIONES:
# definir una funcion
def nombre_funcion (argumento1, argumento2):
    # Aqui iria SANGRADO el contenido de la funcion
    print(argumento1)
    print(argumento2)
# llamar a la funcion
nombre_funcion('Hola','amigo')
nombre_funcion('Adios','amigo')

def suma(a,b):
    return a+b
    
resultado=suma(4,3)
print(resultado)

# Control de flujo
# Condicionales
if 7//3==2:
    print('Es cierto')
else:
    print('No es cierto')


# FUNCION QUE CALCULE EL MAXIMO DE 2 NUMEROS
def maximo(numero1, numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2

def maximo_de_tres(numero1, numero2, numero3):
    return maximo(maximo(numero1,numero2), numero3)

el_mayor=maximo(8,7)
print(el_mayor)


el_mayor=maximo_de_tres(48,7,21)
print(el_mayor)

# Control de flujo... condicionales
# Control de flujo... bucles
mi_lista=(1,2,3,4,5,6)  # Tupla

for numero in mi_lista:
    print(numero)

for numero in range(1,100,5):
    print(numero)

mi_lista=('ivan','rafael','sara') # TUPLA
for nombre in mi_lista:
    print(nombre)


mi_lista=['ivan','rafael','sara'] # LISTA
for nombre in mi_lista:
    print(nombre)

# Las tuplas son INMUTABLES (Como constantes, no se pueden cambiar), las listas SI
mi_lista[1]='Luis'

# BUCLE: while
numero=10
while numero>0:
    print(numero)
    numero=numero-1
    
    
valor_del_usuario=input("Dame un valor")
print(valor_del_usuario)