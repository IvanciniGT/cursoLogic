
"""
Bienvenido, deme un servidor para conectarme [localhost]: _
Ahora el puerto del servidor [7001]: _
Por ultimo, deme un nombre de dominio: _
Por favor, necesito un nombre de dominio: _
(como mucho 3 veces), si no se obtiene en 3 veces. Le muestro un error:
    ERROR: No se ha conseguido un nombre de dominio válido. ABORTANDO...
"""

def conectar(servidor='', puerto='', dominio=''):
    # Pida al usuario:
    #   Servidor -> localhost
    if servidor == '':
        servidor=input('Bienvenido, deme un servidor para conectarme [localhost]: ')
        if servidor == '':
            servidor='localhost'
    print('   Establecido como servidor el valor: ' + servidor)

    #   Puerto   -> 7001
    if puerto == '':
        puerto=input('Ahora el puerto del servidor [7001]: ')
        if puerto == '':
            puerto='7001'
    print('   Establecido como puerto el valor: '+str(puerto))
    
    #   Dominio  -> Le vuelva a preguntar hasta que introduzca uno
    # for intento in range(3,0,-1): # 3, 2, 1
    intento=3
    while dominio == '':
        dominio=input('Por favor, necesito un nombre de dominio: ')
        if dominio == '':
            #intento = intento - 1
            intento-= 1  # -= += *= /=
            if intento==0:
                print('ERROR: No se ha conseguido un nombre de dominio válido. ABORTANDO...')
                break
            else:
                print('No ha introducido un dominio valido. Le quedan '+intento+' disponibles')

    print('   Establecido como dominio el valor: '+ dominio)
        
    # Conexión a WEBLOGIC

conectar(servidor='miweblogic.prod', dominio='MIDOMINIO')