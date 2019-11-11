from django.test import TestCase
from .models import Payment_food
import unittest

# Create your tests here.

def test_rut(a):
        status = ''
        list = Payment_food.objects.all()
        for x in list:
            if x.rut == a:
                status = 'ENCONTRADO'
                
            else:
                status = 'NO ENCONTRADO'
        return status



class TestProbar(unittest.TestCase):
    def test_comparativo(self):
        print('Ingrese el rut a buscar:')
        x = input()
        self.assertEqual(test_rut(x),'ENCONTRADO')