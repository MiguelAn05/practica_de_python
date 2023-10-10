num = 10
flt = 1.5
bol = True
cd = "Hola ADA"

concatenar = cd + str(num) + " " + str(flt) + " " + str(bol)


# Imprimir el resultado de la concatenación
print("Concatenación de variables:")
print(concatenar)


# Límite de enteros: En Python, los enteros tienen un límite superior y inferior que depende de la arquitectura de tu sistema. En sistemas de 32 bits, el límite superior es 2,147,483,647 y el límite inferior es -2,147,483,648. En sistemas de 64 bits, el límite es mucho mayor.
# Límite de flotantes: Python utiliza el estándar IEEE 754 para representar números de punto flotante. El límite superior para los flotantes positivos es aproximadamente 1.8 x 10^308, y el límite inferior para los flotantes positivos es aproximadamente 5.0 x 10^-324.


n = 10  
suma_pares = n * (n + 1)

print("\nSuma de los primeros", n, "números pares:")
print(suma_pares)
