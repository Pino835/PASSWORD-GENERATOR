import random
import string

def generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    # Caracteres básicos (letras minúsculas)
    caracteres = string.ascii_lowercase
    
    # Agregar caracteres adicionales según la selección del usuario
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Generar la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("Bienvenido al generador de contraseñas")
    
    # Pedir al usuario la longitud de la contraseña
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if longitud <= 0:
                print("Por favor, ingrese un número positivo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Preguntar al usuario si desea incluir diferentes tipos de caracteres
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'
    
    # Generar y mostrar la contraseña
    contrasena = generar_contrasena(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    print(f"Contraseña generada: {contrasena}")

if __name__ == "__main__":
    main()