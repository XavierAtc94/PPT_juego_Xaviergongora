# PPT_juego_Xaviergongora
🎮 Piedra, Papel o Tijera

## 📅 Fecha
Abril 2026

## 🎯 Objetivo del programa
Crear un juego interactivo de "Piedra, Papel o Tijera" donde el usuario compite contra la computadora, con validaciones de entrada para evitar errores y la opción de jugar múltiples rondas.

## ⚙️ Principales funcionalidades


`import random` :Permite generar números aleatorios para la jugada de la computadora
`opciones = {1: "🪨 Piedra", 2: "📄 Papel", 3: "✂️ Tijera"}` :Diccionario que almacena las opciones del juego para facilitar su uso
`while respuesta not in ["s", "n"]`: Bucle que valida que el usuario ingrese solo 's' o 'n' al preguntar si quiere jugar
`jugar = respuesta.lower() == "s"` : Variable booleana que determina si el juego continúa
`while jugar:`: Bucle principal que mantiene el juego activo mientras el usuario quiera seguir jugando
Validación de jugada: Bucle `while` que verifica que el usuario elija 1, 2 o 3
`random.randint(1,3)`: Genera la jugada aleatoria de la computadora
Condicionales `if/elif/else`: Determinan si hay empate, derrota o victoria según las reglas del juego
Pregunta de repetición: Al finalizar la ronda, pregunta si se quiere jugar otra vez validando 's' o 'n'

## 🕹️ Reglas del juego
- **Piedra (1)** vence a **Tijera (3)**
- **Papel (2)** vence a **Piedra (1)**
- **Tijera (3)** vence a **Papel (2)**

## ▶️ Cómo ejecutar
```bash
python piedra_papel_tijera.py
