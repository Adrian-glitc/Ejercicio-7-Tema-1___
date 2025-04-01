class Inventario:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        if item in self.items:
            raise ValueError(f"El ítem '{item}' ya está en el inventario.")
        self.items.append(item)