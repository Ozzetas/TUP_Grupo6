# Importa el módulo time para usar la función sleep, que permite pausar la ejecución.
import time

# Define una variable que establece el tiempo de pausa (en segundos) entre cada iteración.
tiempo = 1

# Imprime un título y una descripción del programa, indicando que mostrará los números del 0 al 15 en formato binario.
print("Contador Binario:\nEl programa mostrara los números decimales del 0 al 15 en binario:")

# Inicializa la variable numero_binario como un string vacío para almacenar la representación binaria de cada número.
# Inicializa la variable numero en 0 para llevar un conteo auxiliar de los números decimales (usada en la impresión).
numero_binario = ""
numero = 0

# Inicia un ciclo for que itera desde 0 hasta 15 (range(16) genera números de 0 a 15).
for i in range(16):
    # Verifica si el número actual (i) es 0, ya que el 0 en binario es un caso especial ("0").
    if i == 0:
        # Asigna directamente "0" a numero_binario, ya que no requiere cálculo.
        numero_binario = "0"
        # Imprime el número decimal (i) y su representación binaria (numero_binario).
        print(f"El numero decimal {i} en binario es: {numero_binario}")
    else:
        # Reinicia numero_binario como un string vacío para construir la representación binaria del número actual.
        numero_binario = ""
        # Inicia un ciclo while que continúa mientras el número (i) sea mayor que 0.
        while i > 0:
            # Calcula el resto de dividir i entre 2 (0 o 1) y lo concatena al inicio de numero_binario como string.
            numero_binario = str(i % 2) + numero_binario
            # Actualiza i dividiéndolo entre 2 (división entera) para obtener el siguiente dígito binario.
            i = i // 2
        # Incrementa la variable numero en 1 para usarla en la impresión del número decimal.
        numero = numero + 1
        # Imprime el número decimal (usando la variable numero) y su representación binaria.
        print(f"El numero decimal {numero} en binario es: {numero_binario}")
        # Pausa la ejecución por el tiempo definido (1 segundo) para mostrar los resultados de forma pausada.
        time.sleep(tiempo)