#Se importa el modulo del tiempo
import time
#Se crea la variable tiempo para despues utilizarla con la funcion time.sleep()
tiempo = 1
#Se imprime por pantalla un titulo del programa y lo que hara
print("Contador Binario:\nEl programa mostrara los números decimales del 0 al 15 en binario:")
#Definimos e inicializamos las variables
numero_binario = ""
numero = 0
#Iniciamos el ciclo For que itera los numeros del 0 al 15
for i in range(16):
    #Se crea un condicional que si el numero en el ciclo for es igual a 0, le asignamos
    #a numero_binario un string con el cero entre comillas.
    if i == 0:
        numero_binario = "0"
        #imprimimos por pantalla el numero decimal que itera en el ciclo, en binario
        print(f"El numero decimal {i} en binario es: {numero_binario}")
    else:
        numero_binario = ""
        while i > 0:
            #Calculamos el resto y lo convertimos a String para poder concatenarlo en lugar de sumarlo
            numero_binario = str(i % 2) + numero_binario
            #Calculamos el cociente de la division entera
            i = i // 2
        #Le sumamos un 1 a la variable numero para poder mostrarlo por pantalla
        numero = numero + 1
        print(f"El numero decimal {numero} en binario es: {numero_binario}")
        #Utilizamos la funcion time.sleep() para retardar 1 segundo cada ciclo
        time.sleep(tiempo)