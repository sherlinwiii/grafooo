def crear_grafo():
    conexiones = [
        ("CDMX", "EdoMex", 50), ("CDMX", "Puebla", 80), ("CDMX", "Querétaro", 200),
        ("EdoMex", "Guerrero", 180), ("EdoMex", "Querétaro", 150), ("Querétaro", "Guanajuato", 100),
        ("Guerrero", "Puebla", 300), ("Guerrero", "Michoacán", 250), ("Puebla", "Veracruz", 120),
        ("Veracruz", "Michoacán", 400), ("Guanajuato", "Michoacán", 150)
    ]
    return conexiones

def mostrar_grafo(conexiones):
    print("Estados y sus conexiones:")
    for origen, destino, costo in conexiones:
        print(f"{origen} - {destino} : {costo} km")
    
    print("\nRepresentación del Grafo:")
    nodos = set()
    for origen, destino, _ in conexiones:
        nodos.add(origen)
        nodos.add(destino)
    
    for nodo in nodos:
        print(f"{nodo}: ", end="")
        for origen, destino, costo in conexiones:
            if origen == nodo:
                print(f"({destino}, {costo}km) ", end="")
            elif destino == nodo:
                print(f"({origen}, {costo}km) ", end="")
        print()

conexiones = crear_grafo()
mostrar_grafo(conexiones)

print("Grafo generado y mostrado correctamente.")


