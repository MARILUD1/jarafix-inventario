
# Módulo de Gestión de Inventario de Repuestos - JaraFix

class Repuesto:
    def __init__(self, id_repuesto, nombre, stock_actual, stock_minimo, precio):
        self.id_repuesto = id_repuesto
        self.nombre = nombre
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.precio = precio
    
    def verificar_stock(self):
        """Verifica si el stock está por debajo del mínimo"""
        return self.stock_actual < self.stock_minimo
    
    def descontar_stock(self, cantidad):
        """Descuenta cantidad del stock actual"""
        if cantidad > self.stock_actual:
            raise ValueError("No hay suficiente stock")
        self.stock_actual -= cantidad
        return self.stock_actual
