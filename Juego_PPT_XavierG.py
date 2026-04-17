import random #Para que el programa pueda generar numeros o listas aleatorios
opciones = {1: "🪨 Piedra",2: "📄 Papel",3: "✂️ Tijera"}
print("Piedra, papel o tijera") #Bienvenida del juego e inicio

respuesta = input("\n¿Quieres jugar? (s/n): ") #Determino las opciones para jugar siendo s= sí y n= no
while respuesta not in ["s", "n"]: #condicional de opciones validas
        print("Opción inválida, escribe 's' o 'n'")
        respuesta = input("Intenta de nuevo: ").lower()
jugar = respuesta.lower () == "s" #Variable jugar es s minuscula , lowe convierte mayuculas a mainusculas

while jugar:
    print("Elige: 1 = Piedra, 2 = Papel, 3 = Tijera") #determino las opciones que tiene el jugador
    jugador = input("Tu elección: ") #ingresa un número para elegir  
    
    while jugador not in ["1", "2", "3"]: #si no es 1, 2 o 3 va dar error, evitamos eso con este while
        print("Opción inválida, debes elegir 1, 2 o 3") #retorna el error del usuario
        jugador = input("Vuelve a elegir: ") #para que pueda volver a elegir   
    jugador = int(jugador) #ingresa como número entero
    pc= random.randint (1,3) #genera un número aleatorio la pc
    print(f"Tú elegiste: {opciones[jugador]}")
    print(f"La PC eligió: {opciones[pc]}")
    if jugador == pc: #primer condicional, si son iguales da empate, usaremos elif para lo siguiente
        print ("🤝 Empate")
    elif (jugador==1 and pc==2) or (jugador==2 and pc==3) or (jugador==3 and pc==1):#opciones de perdida
        print ("💀 Perdiste")
    else:
        print ("🏆 Ganaste") #si sale alguna otra opción, ganamos
    respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()

    while respuesta not in ["s", "n"]: #condicional de opciones validas
        print("Opción inválida, escribe 's' o 'n'")
        respuesta = input("Intenta de nuevo: ").lower()
    jugar = respuesta == "s"
print("Saliendo") #fin del juego
