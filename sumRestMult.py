#!C:\Users\zx22student3203\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = sumar(num1, num2)
    print("La suma es:", resultado)

def restar(a, b):
    return a - b

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = restar(num1, num2)
    print("La resta es:", resultado)
    
def multiplicar(a, b):
    return a * b

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = multiplicar(num1, num2)
    print("La multiplicación es:", resultado)