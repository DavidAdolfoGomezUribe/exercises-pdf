#Ejercicio 3: Calculadora básica
#Utiliza match para implementar una calculadora simple.
#Enunciado:
#Crea una calculadora que solicite dos números y una operación matemática (+, -, *, /). Usa match
#para realizar la operación correspondiente.


name = input("Hello,please enter your name: ")
while True:
    try:
        
        
        print(f"""Hello Mrs/Ms {name} this is a program for a basic calculator.
                select the operation that you want todo (+,-,/,*)""")
        
        variable = str(input(""))
        match variable:
            case "+":
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                total = a + b
                print(f"        your total is {total} ")
            case "-":
                pass
            case "/":
                pass
            case"*":
                pass
                                
    except:
        print("        Please enter a valid number") 
    
    
