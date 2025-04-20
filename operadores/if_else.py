number = int(input('Ingrese un numero: '))


    
if number>0:
    if number%2==0:
        print(f"El numero {number} es par positivo.")
    else:
        print(f"El numero {number} es impar positivo.")
elif number<0:
    if number%2==0:
        print(f"El numero {number} es par negativo.")
    else:
        print(f"El numero {number} es impar negativo.")
    
else:
    print("El numero es cero")
    
    