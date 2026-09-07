"""
Prueba automatizada del caso crítico CP-02
Módulo: Gestión de Inventario de Repuestos - JaraFix
Caso: Descuento de stock válido (RF-05)
"""
import sys
import os
import unittest

# Agregar la ruta correcta para importar desde src/src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'src'))

from inventario import Repuesto


class TestCP02_DescuentoStockValido(unittest.TestCase):
    """
    CP-02: Caso más crítico del módulo
    Valida que el método descontar_stock() funcione correctamente
    cuando se solicita una cantidad válida (menor o igual al stock disponible).
    """
    
    def test_cp02_descuento_stock_valido(self):
        """
        Entrada: Repuesto con stock_actual=20, stock_minimo=10, precio=25.00
        Pasos: Ejecutar descontar_stock(5)
        Resultado esperado: Retorna 15 (20 - 5 = 15) y no lanza excepción
        Valida: RF-05
        """
        # Arrange: Crear el objeto Repuesto
        repuesto = Repuesto(
            id_repuesto=2,
            nombre="Aceite de motor",
            stock_actual=20,
            stock_minimo=10,
            precio=25.00
        )
        
        # Act: Ejecutar el método de descuento
        nuevo_stock = repuesto.descontar_stock(5)
        
        # Assert: Verificar el resultado esperado
        self.assertEqual(nuevo_stock, 15, 
                        "El stock debe reducirse de 20 a 15 unidades")
        self.assertEqual(repuesto.stock_actual, 15,
                        "El atributo stock_actual debe actualizarse a 15")


if __name__ == '__main__':
    unittest.main()
