from django.test import TestCase
from apl.models import Categoria

class PruebaBasica(TestCase):
    def test_verificar_entorno(self):
        """Una prueba simple para validar que CI/CD funciona"""
        self.assertEqual(1 + 1, 2)
    
    def test_crear_categoria(self):
        """prueba basica de base de datos en memoria"""
        #las consultas e imserciones van dentro de las funciones
        Categoria.object.create(nombre='Frijol')
        consulta = Categoria.objects.filter(nombre='Frijol')
        self.assertTrue(consulta.exists())
    