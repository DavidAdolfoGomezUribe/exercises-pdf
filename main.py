#Ejercicio 1: Verificación de números pares e impares
#Escribe un programa que verifique si un número es par o impar utilizando if .
#Enunciado:
#Solicita al usuario que ingrese un número y verifica si es par o impar.


name = input("Hello,please enter your name:")
while True:
    try:
        print(f"Hello Mrs/Ms {name} this is a program for calculate if a number is even or odd.")
        number = float(input("        Enter the number: "))
    
        if number % 2 == 0:
            print(f"        Your number {number} is even.")
            break
        else:
            print(f"        Your number {number} is odd")
            break
        
    except:
        print("        Please enter a valid number") 
    
    
    