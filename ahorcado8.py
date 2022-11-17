import random

seguirJugando = True

while seguirJugando == True: # Este es el bucle del menú
    print("┌"+"─"*55+"┐")
    print("│"+" "+"JUEGO DEL AHORCADO"+" "*36+"│")
    print("└"+"─"*55+"┘")
    escenario = """
        ┌──────┐       │  J U E G O  D E L  A H O R C A D O
        │      │       │  Tema: comidas
        │      O       │  MENU DE OPCIONES
        │     /│\      │    1.- Jugar al ahorcado
        │     / \      │    2.- Reglas del juego
        │              │    3.- Integrantes del grupo
        │              │    4.- Salir del juego
       ─┴────────────  │
    """
    print(escenario)
    print("")
    opcion = int(input("Ingresá tu opción: "))
    if opcion == 1:  # Esta es el juego en si que está inserto dentro del menú
        
        ######## FUNCIONES ########

        def escenario(vidas, fallidas, p1, p2, p3, p4, p5, p6, secreta): # Esta función es la que pinta el escenario principal
            print("┌"+"─"*55+"┐")
            print("│"+" "+"JUEGO DEL AHORCADO"+" "*36+"│")
            print("└"+"─"*55+"┘")
            escenario = f"""
             ┌──────┐       │
             │      │       │  Tema: comidas
             │      {p1}       │  Tus vidas: {vidas} - {vidasACorazones(vidas)}      
             │     {p2}{p3}{p4}      │  Letras fallidas: {fallidas}
             │     {p5} {p6}      │
             │              │  Tu palabra: {secreta}
             │              │ 
            ─┴────────────  
            """
            print(escenario)

        def develarLetra(palabra, letra, incognita): 
            contador = 0
            incognita = list(incognita)
            while contador < len(incognita):
                if incognita[contador] == "_" and letra == palabra[contador]:
                    incognita[contador] = letra
                contador += 1
            incognita = "".join(incognita)
            return incognita

        def vidasACorazones(vidas):
            indice = vidas
            corazones = []
            while indice > 0:
                corazones.append('❤  ')
                indice -= 1
            corazones = "".join(corazones)
            return corazones







        ######## VARIABLES ########

        comidas = ["asado", "ensaladas", "empanadas", "tarta", "milanesas", "ravioles", "cordero", "fideos", "locro", "tallarines"]
        vidas= 7
        letrasFallidas = []
        letrasAcertadas = []
        p1 = " " # O
        p2 = " " # / 
        p3 = " " # │
        p4 = " " # \
        p5 = " " # /
        p6 = " " # \
        comidaAlAzar = "" # En esta variable cargaremos la palabra a adivinar
        palabraSecreta = [] # Variable q tendrá solo "_" y las letras que vaya descubriendo, mostrar en el escenario
        letraUsuario = "" # Esta variable es para lo  vaya ingresando el usuario 





        ######## PROGRAMA ########

        # Elegimos una comida al azar
        comidaAlAzar = random.choice(comidas) # Elijo una palabra de la lista

        # Pasamos la palabra a guiones
        for letra in comidaAlAzar:
            palabraSecreta.append("_") # con el for agregamos un "_" por cada letra a la palabra secreta
        palabraSecreta = "".join(palabraSecreta) # Transformamos la palabra secreta, de lista a string con el join
            


        # BUCLE PRINCIPAL
        while vidas > 0 :

            # print(f"(Ayuda. La palabra es {comidaAlAzar})") # Esta línea es para ayudar con la palabra
            escenario(vidas, letrasFallidas, p1, p2, p3, p4, p5, p6, palabraSecreta) # Comenzamos mostrando el escenario inicial

            letra = input("Ingresá una letra o arriesgá una palabra: ") #  Ingreso del usuario
            letraUsuario = letra.lower() # Paso lo que haya ingresado el usuario a minúscula
            
            while letraUsuario in letrasFallidas or letraUsuario in letrasAcertadas: # Con este bucle obligo a que la letra ingresada no esté repetida
                letra = input(f"La letra {letraUsuario} ya la ingresaste anteriormente, ingresá una nueva: ")
                letraUsuario = letra.lower() # Paso a minúscula lo que se ingresa por teclado
            
            while letraUsuario.isalpha() == False: # Con este bucle obligo a que sea una letra solamente
                letra = input(f"{letraUsuario} no es una letra/palabra válida. Volver a ingresar: ")
                letraUsuario = letra.lower()  # Paso a minúscula lo que se ingresa por teclado


        # Aquí comienza el rollo...
            # Si ingresa solo una letra...
            if len(letraUsuario) == 1:
                if letraUsuario in comidaAlAzar: # Si la letra está en la palabra
                    palabraSecreta = develarLetra(comidaAlAzar, letraUsuario, palabraSecreta) # Voy a la función que muestra la letra acertada
                    letrasAcertadas.append(letraUsuario) # Agrego la letra acertada a la lista de acertadas
                    escenario(vidas, letrasFallidas, p1, p2, p3, p4, p5, p6, palabraSecreta) # Muestro el escenario refrescado
                    if palabraSecreta.count("_") == 0: # Chequeo que ya no haya más letras para adivinar
                        print(f"GENIAL.... tu palabra era {comidaAlAzar}")
                        break
                else:
                    vidas -= 1 # Resto una vida por el error
                    letrasFallidas.append(letraUsuario) # Agrego la letra a la lista de letras fallidas
                    if vidas == 6: # si le quedan 6 vidas, pongo la cabeza del ahorcado
                        p1 = "O"
                    elif vidas == 5: # si le quedan 5 vidas, le pongo un brazo....
                        p2 = "/"
                    elif vidas == 4:
                        p3 = "│"
                    elif vidas == 3:
                        p4 = "\\" # Aqui el simbolo es doble para escapar la barra, para que no la confunda con un salto de línea
                    elif vidas == 2:
                        p5 = "/"
                    elif vidas == 1:
                        p6 = "\\"
                    elif vidas == 0 : # Acá ya perdió
                        palabraSecreta = comidaAlAzar # develo la palabra para mostrarla en el escenario
                        escenario(vidas, letrasFallidas, p1, p2, p3, p4, p5, p6, palabraSecreta) # Muestro escenario con la palabra q no acertó
                        print(f"PERDISTE !!! tu palabra era {comidaAlAzar}")
                        break
            # Si ingresa una palabra...
            else: # Si ingresa una cadena de más de una letra...
                if letraUsuario == comidaAlAzar: # lo que ingresó el usuario es una palabra
                    palabraSecreta = comidaAlAzar # Develo la palabra para mostrarla en el escenario
                    escenario(vidas, letrasFallidas, p1, p2, p3, p4, p5, p6, palabraSecreta) # Refresco el escenario
                    print(f"GENIAL.... tu palabra era {comidaAlAzar}")
                    break #salimos....
                else: # Si erra la palabra...
                    vidas -= 3 # Resto 3 vidas según la consigna
                    letrasFallidas.append(letraUsuario) # Agrego la palabra a la lista de fallos
                    if vidas == 4: # Como son 3 las vidas que resto, nunca le pueden quedar 6 o 5, comenzamos por el 4
                        p1 = "O"
                        p2 = "/"
                        p3 = "│"
                    elif vidas == 3:
                        p2 = "/"
                        p3 = "│"
                        p4 = "\\"
                    elif vidas == 2:
                        p3 = "│"
                        p4 = "\\"
                        p5 = "/"
                    elif vidas == 1:
                        p4 = "\\"
                        p5 = "/"
                        p6 = "\\"
                    if vidas <= 0 : # Acá ya perdió
                        palabraSecreta = comidaAlAzar # Develamos la palabra
                        escenario(vidas, letrasFallidas, p1, p2, p3, p4, p5, p6, palabraSecreta) # Pintamos el escenario refrescado.
                        print(f"PERDISTE !!! tu palabra era {comidaAlAzar}")
                        input("(Presione ENTER para continuar)")
                        break
    elif opcion == 2:
        print("┌"+"─"*55+"┐")
        print("│"+" "+"JUEGO DEL AHORCADO"+" "*36+"│")
        print("└"+"─"*55+"┘")
        print("REGLAMENTO")
        print("\tObjetivo: consiste en acertar la frase secreta sin cometer más de siete fallos.")
        print("\tTipo de prueba: Una palabra oculta por partida con un máximo de 22 caracteres y 4 palabras.")
        print("\tTurno:")
        print("\t- En su turno el jugador puede: colocar una letra / Adivinar la palabra. ")
        print("\tColocar una letra: El jugador ingresa una letra: ")
        print("\t-- Si la letra es correcta, se completa en la palabra(todas las veces que aparece) y se sigue con el juego")
        print("\t-- Si la letra es incorrecta, se resta un corazón.")
        print("\tAdivinar la Palabra: El jugador puede intentar adivinar la palabra o frase secreta.")
        print("\t-- Si ingresa la palabra correcta, entonces el jugador gana.")
        print("\t-- Si ingresa la palabra incorrecta, entonces se restan 3 corazones.")
        print("")
        print("Fin de la partida:")
        print("\t- GANA el jugador si descubre la palabra o frase secreta. ")
        print("\t- PIERDE el jugador se restan los 7 corazones")
    elif opcion == 3:
        print("┌"+"─"*55+"┐")
        print("│"+" "+"JUEGO DEL AHORCADO"+" "*36+"│")
        print("└"+"─"*55+"┘")
        print("INTEGRANTES")
        print("\tAna Raquel Maldonado")
        print("\tClaudia Sivilotti")
        print("\tMercedes Estela Scipioni")
        print("\tFlorencia Castro")
        print("\tMarcelo Berretta")
    elif opcion == 4:
        print("Gracias por jugar...")
        seguirJugando = False