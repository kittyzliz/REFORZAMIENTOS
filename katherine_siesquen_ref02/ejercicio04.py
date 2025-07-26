radio = float(input("Ingrese el radio de la esfera: "))
radio_cubico = pow(radio, 3)
volumen = (4/3) * 3.14159 * radio_cubico

print("El volumen de la esfera es: ", round(volumen, 2))
