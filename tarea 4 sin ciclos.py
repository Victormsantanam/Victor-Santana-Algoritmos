"""Un año es bisiesto si es divisible entre 4 excepto si es divisible entre 100 y no por 400.
 Haga el diagrama de flujo de, e implemente en Visual Studio Code, un programa que reciba como entrada un año entre 1900 y 2199
   y además calcule el número de años bisiestos entre 1900 y el año de entrada 
   (restando de los años posibles todos los que no son bisiestos).

Por ejemplo, el número de años bisiestos hasta 1992 son 23, mientras que el de 2199 son 93.

Recuerde que // da el cociente de la división y % da el residuo

Debe implementar dos versones del programa: una que use ciclos, y una que no los use."""

print("Programa para determinar si un año es bisiesto.")
año = int(input("Ingrese un año entre 1900 y 2199: "))
años = año - 1900 + 1
bisiesto = (años//4) - (años//100) + (años//400)
if año < 1900 or año > 2199: 
    print(" El numero que ingresaste es incorrecto.")
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0 :
    print (f"El año ", {año}, "es bisiesto y el numero de años bisiestos que hay hasta ese año es: ", {bisiesto})
else: 
    print(f"El año ", {año}, "no es bisiesto y el numero de años bisiestos que hay hasta ese año es: ", {bisiesto})