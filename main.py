import random
import time

# colores
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
# dos valores aleatorios para hacerlo interesante
s = random.randint(1, 10)
s1 = random.randint(1, 10)

# variables para las respuesta correctas e incorrectas respectivamente
correcta = BLUE + 'RESPUESTA CORRECTA' + RESET
error = RED + 'RESPUESTA INCORRECTA' + RESET

# varibles para el bucle
iniciar_programa = True
n_intentos = 0

# comienzo del bucle
while iniciar_programa == True:
    n_intentos += 1

    print('Bienvenido a mi trivia ramdom')
    print('intento numero :', n_intentos)
    time.sleep(2)
    if n_intentos == 1:
        nombre = input(MAGENTA + 'Cual es tu nombre jugador?:  ' + RESET)
        while nombre == '':
                nombre = input(MAGENTA + 'Ingrese un nombre valido:  ' + RESET)

        print('''Un gusto''', nombre,
              '''Para comenzar te dare un par de instrucciones''',
              RED + '''presta mucha atencion''', RESET + '')
    else:
        print('HOLA DE NUEVO', nombre)
        print('''Bueno ya sabes como va esto''', nombre,
              RED + '''presta mucha atencion''', RESET + '')
    time.sleep(2)

    print(
        '''para responder escribe la letra de la alternativa correcta y pulsa[ENTER] para enviar tu respuesta 
cada pregunta tiene un puntaje aleatorio...podras ver tu puntaje en pantalla.'''
    )
    # variable que indica la puntuacion dentro del bucle para reiniciarse
    score = 0
    time.sleep(2)
    print('''Estas listo???''')

    time.sleep(1)
    input('''presiona [ENTER] para inciar''')

    print('tu puntaje es:' + str(score))
    # uso de for para crear una cuenta regresiva
    for a in range(4, 2, -1):
        print(RED, +a, 'cargando datos')
        time.sleep(1)
    for a in range(2, -1, -1):
        print('', a, '.....ya casi')
        time.sleep(1)

# aqui comiencian las preguntas
# magenta y reset variables para controlar el color
    print(
        MAGENTA + '''¿Quien  fue el primer hombre en la luna?''', RESET + '''
         a) Neil Alden Armstrong
         b) Homero Simpson
         c) Bartolome Lin
         d) Neil deGrasse Tyson
         ''')
    # .lower para forzar las minusculas y no pedir al jugador que cambie de mayusculas a minusculas
    respuesta_1 = str.lower(input("tu respuesta: "))

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = str.lower(
            input(
                "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            ))

    if respuesta_1 == 'a':
        print(correcta, 'Asi es ahi es cuando dijo su iconica frase:.......')
    else:
        print(error, 'Homer tal vez en la ficcion, Neil Tyson es un fisico')
# cada repuesta obtiene dos posibles puntajes 0 o 1
    if respuesta_1 == 'a':
        # a la variable score la sumo o resto las variables con los puntajes aleatorios
        score += s

    else:
        score -= s1

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA + '''¿Quien es el creador de paypal?''', RESET + '''
         a) Nickola Tesla
         b) Leonardo da Vinci
         c) Elon Musk
         d) Pablo Pickaso
         ''')
    respuesta_2 = str.lower(input("tu respuesta: "))

    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = str.lower(
            input(
                "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
            ))

    if respuesta_2 == 'c':
        print(correcta, 'Bueno tampoco estaba muy dificil')
    else:
        print(error, ' Como fallaste.....')
    if respuesta_2 == 'c':
        score += s
    else:
        score -= s

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA + ''' ¿Cuántas franjas tiene la bandera de Estados Unidos?''',
        RESET + '''
             a) 15
             b) 13
             c) 3
             d) 30
             ''')
    respuesta_3 = str.lower(input("tu respuesta: "))

    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_3 == 'b':
        print(correcta, 'en honor a los trece estados')
    else:
        print(error, 'Te falta ver mas series ')
    if respuesta_3 == 'b':
        score += s1
    else:
        score -= s

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA +
        '''4) ¿Cuál de los siguientes imperios no tenía un idioma escrito: 
                  Inca, Aztecas, Egipcios, Romanos?''', RESET + '''
             a) Inca
             b) Azteca
             c) Egipcios
             d) Romanos
             ''')
    respuesta_4 = str.lower(input("tu respuesta: "))

    while respuesta_4 not in ("a", "b", "c", "d"):
        # lo mismo .lower para minusculas en la segunda entrada de datos( no sabia que funcionara asi)
        respuesta_4 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_4 == 'a':
        print(correcta, 'ASI es los incas usaban los quipus')
    else:
        print(error, 'Pachacutec estaria furioso')
    if respuesta_4 == 'a':
        score += s1
    else:
        score -= s

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA + ''' ¿Cuál es el río más largo del mundo?''', RESET + '''
             a) Missisipi
             b) Nilo
             c) Amazonas
             d) Estigia
             ''')
    respuesta_5 = str.lower(input("tu respuesta: "))

    while respuesta_5 not in ("a", "b", "c", "d"):
        respuesta_5 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_5 == 'b':
        print(correcta, 'no confundir con el mas caudaloso que es el Amazonas')
    else:
        print(error, 'si, yo tambien falle....')
    if respuesta_5 == 'b':
        score += s
    else:
        score -= s1

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA +
        '''¿Cómo le llaman los locales a la Ciudad de Nueva York por la noche?''',
        RESET + '''
             a) La Gran Manzana
             b) Las Vegas
             c) La Ciudad del amor
             d) Gotham
             ''')
    respuesta_6 = str.lower(input("tu respuesta: "))

    while respuesta_6 not in ("a", "b", "c", "d"):
        respuesta_6 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_6 == 'd':
        print(
            correcta,
            'Woa no lo esperaba,los neoyorquinos la llaman asi por el murcielago mas famoso'
        )
    else:
        print(error, 'Bueno era una pregunta trampa no te preocupes')
    if respuesta_6 == 'd':
        score += s1
    else:
        score -= s

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA + '''7)¿Cuál es la obra más famosa de Edvard Munch?''',
        RESET + '''
             a) La monalisa
             b) El Grito
             c) La Creacion
             d) El Hombre de Vitruvio
             ''')
    respuesta_7 = str.lower(input("tu respuesta: "))

    while respuesta_7 not in ("a", "b", "c", "d"):
        respuesta_7 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_7 == 'b':
        print(correcta, 'Edvard estaria orgulloso')
    else:
        print(error, 'bueno al menos sabes tu nombre')
    if respuesta_7 == 'b':
        score += s1
    else:
        score -= s

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA + '''8)¿Quién inventó la World Wide Web, y cuándo?''',
        RESET + '''
             a) Issac Newtom ,1458
             b) Albert Einstem ,1945
             c) Alan Turing, 1996
             d) Tim Berners-Lee, 1990
             ''')
    respuesta_8 = str.lower(input("tu respuesta: "))

    while respuesta_8 not in ("a", "b", "c", "d"):
        respuesta_8 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_8 == 'd':
        print(correcta, 'acaso eres el nerd legendario')
    else:
        print(error, ' apuesto que pensaste que era Alan Turing')
    if respuesta_8 == 'd':
        score += s

    else:
        score -= s1

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA + '''9)¿Cuántas teclas tiene un piano?''', RESET + '''
             a) 50
             b) 53
             c) 59
             d) 88
             ''')
    respuesta_9 = str.lower(input("tu respuesta: "))

    while respuesta_9 not in ("a", "b", "c", "d"):
        respuesta_9 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_9 == 'd':
        print(correcta, 'aunque solo en un piano convencional')
    else:
        print(error, 'vale la musica no es lo tuyo')
    if respuesta_9 == 'd':
        score += s1
    else:
        score -= s

    print('tu puntaje es:' + str(score))

    time.sleep(1)
    input('[ENTER] para continuar')

    print(
        MAGENTA +
        '''10)¿En que serie anime el protagonista pelea contra algeles gigantes?''',
        RESET + '''
             a) Naruto SHIPUDEN
             b) V de Vendetta
             c) Evangelion
             d) Dragon Ball
             ''')
    respuesta_10 = str.lower(input("tu respuesta: "))

    while respuesta_10 not in ("a", "b", "c", "d"):
        respuesta_10 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_10 == 'c':
        print(correcta, 'una de las series de culto de la ultimas decadas')
    else:
        print(error, 'concentrate')
    if respuesta_10 == 'c':
        score += s
    else:
        score -= s1

    print('tu puntaje es:' + str(score))
    print('tienes una ultima chance de aumentar tus puntos '
          'pero es una apuesta arriesgada!!!!!   '
          'aceptas SI O NO?')
    # aqui se le pide al jugador si quiere apostar
    random.randint(-50, 10)
    opcion_final = input('responde con si o no   ').lower()
    if opcion_final == 'si':
        surprise = random.randint(-50, 10)
        score += surprise
    else:
        print('sabia desicion')

    print('tu puntuacion final es :', score)
    # el jugador obtine un mensaje de acuerdo al rango de su puntaje
    if -100 <= score <= 10:
        print('vale, no es tu dia')
    if 11 <= score <= 20:
        print('suerte o habilidad?')
    elif 20 <= score <= 100:
        print('Menuda suerte debes de tener')
    # peticion para reiniciar el juego en un nuevo intento o dejar de jugar
    print("\n¿QUIRES INTENTARLO DE NUEVO?")
    nuevo_intento = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    if nuevo_intento != "si":
        print("Espero que la hayas pasado genial, hasta la proxima", nombre)
        iniciar_programa = False
    # para quien lea esto gracias por jugar mi trivia estoy seguro que el codigo debe de ser horrible pero me diverti mucho haciendola
    # llevo un par de dias recien con python pero me alegro de haber dado un paso en este mundo incluso si fallo el proceso de seleccion
