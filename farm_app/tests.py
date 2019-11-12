from django.test import TestCase
from .models import Payment_food
from collections import Counter
import unittest

# Create your tests here.

def test_rut(a):
    status = ''
    list = Payment_food.objects.all().filter(rut = a)
    print(list)
    return list

def objects_test():
    cont = 0
    list = Payment_food.objects.all()
    for x in list:
        cont = cont + 1
    return(cont)

def objects_detail_test():
    list = Payment_food.objects.all()
    cnt = Counter()
    for x in list:
       cnt[x] =+1
    return(cnt)
    

#clase encargada de manejar las pruebas 
class TestProbar(unittest.TestCase): 
    def test_comparativo(self): #funcion encargada de visualizar si se encuentra un objeto en particular dentro de la base de datos
        print('Ingrese el rut a buscar:')
        x = input()
        self.assertTrue(test_rut(x))
    
    def test_conteo(self): #función encargada de visualizar la cantidad de 
        list = Payment_food.objects.all()
        print('Cantidad de objetos: '+ str(objects_test()))
        b = 0
        # return(objects_test())
        self.assertGreater(objects_test(), b)
    
    def test_detalle(self):
        # print(objects_detail_test())
        return(print(objects_detail_test()))