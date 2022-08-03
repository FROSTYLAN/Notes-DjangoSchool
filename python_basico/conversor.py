option = input(
    """
    Hola!, ¿Qué quieres hacer? 
            
        1. Convertir soles a dolares.
        2. Convertir dólares a soles.
    """
)
valor_dolar = 3.91

if (option == "1") :
    soles = float(input("¿Cuántos nuevos soles tienes?"))
    dolares = str(round((soles / valor_dolar), 2))
    print(f"Tienes $ {dolares} dólares.")
elif(option == "2"):
    dolares = float(input("¿Cuántos dólares tienes?"))
    soles = str(round((dolares * valor_dolar), 2))
    print(f"Tienes $ {soles} soles.")
else:
    print("Ingresaste una opción incorrecta")