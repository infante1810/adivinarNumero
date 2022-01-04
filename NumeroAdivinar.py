import random
numero = random.randint(1,2)
print(numero)
correcto = False
for i in range(5):
    if correcto == False:
        print("Ingrese el numero que piensa que es:")
        numeroAdivinar = input()
        numeroAdivinar = int(numeroAdivinar)
        if (numeroAdivinar == numero) and (correcto == False):
            print("el numero adivinado es", numero)
            correcto=True
        else:
            print("Intente otra vez")    
