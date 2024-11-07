#Ejercicio 2: Calificación de una nota
#Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando
#if .
#Enunciado:
#Solicita al usuario una calificación y determina si la nota es aprobatoria (>= 60) o reprobatoria (<
#60).


name = input("Hello,please enter your name: ")
while True:
    try:
        print(f"Hello Mrs/Ms {name} this is a program for calculate if you are approved or not base on your final note.")
        note = float(input("        Enter the number: "))
    
        if note < 0 :
            print("        Enter a valid number")
        else:
            if note >= 60:
                print(f"        Your are approvated with a {round(note)} note.")
                break
            else:
                print(f"        Your are reprovated with a {round(note)} note.")
                break
            
    except:
        print("        Please enter a valid number") 
    
    
      