from Inventario import Inventario

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    try:
        inventario.agregar_item("Espada")
        inventario.agregar_item("Escudo")
        inventario.agregar_item("Espada")  # Esto lanzará un ValueError
    except ValueError as e:
        print(e)