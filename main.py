class Inventario:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        if item in self.items:
            raise ValueError(f"El ítem '{item}' ya está en el inventario.")
        self.items.append(item)

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    try:
        inventario.agregar_item("Espada")
        inventario.agregar_item("Escudo")
        inventario.agregar_item("Espada")  # Esto lanzará un ValueError
    except ValueError as e:
        print(e)