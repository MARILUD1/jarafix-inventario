import unittest
import sys
import os

# Agregar la carpeta src al path para poder importar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'src'))

from inventario import Repuesto

class TestRepuesto(unittest.TestCase):
    
    def test_verificar_stock_bajo(self):
        """Test: stock actual menor que mínimo debe retornar True"""
        repuesto = Repuesto(1, "Filtro de aceite", 5, 10, 15.50)
        self.assertTrue(repuesto.verificar_stock())
    
    def test_verificar_stock_ok(self):
        """Test: stock actual mayor que mínimo debe retornar False"""
        repuesto = Repuesto(1, "Filtro de aceite", 15, 10, 15.50)
        self.assertFalse(repuesto.verificar_stock())
    
    def test_verificar_stock_igual(self):
        """Test: stock actual igual al mínimo debe retornar False"""
        repuesto = Repuesto(1, "Filtro de aceite", 10, 10, 15.50)
        self.assertFalse(repuesto.verificar_stock())
    
    def test_descontar_stock_exitoso(self):
        """Test: descontar stock correctamente"""
        repuesto = Repuesto(1, "Filtro de aceite", 20, 10, 15.50)
        nuevo_stock = repuesto.descontar_stock(5)
        self.assertEqual(nuevo_stock, 15)
    
    def test_descontar_stock_insuficiente(self):
        """Test: intentar descontar más del disponible debe generar error"""
        repuesto = Repuesto(1, "Filtro de aceite", 5, 10, 15.50)
        with self.assertRaises(ValueError):
            repuesto.descontar_stock(10)

if __name__ == '__main__':
    unittest.main()
