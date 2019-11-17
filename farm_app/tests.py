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

def add_objects():
    status = True
    print('Ingrese el rut del objeto')
    rut = input()
    print('Ingrese el numero de cuenta')
    num_cuenta = input()
    print('Ingrese el correo electronico')
    correo = input()
    selector = 'Dapac Cerdas'
    selector2 = 'Tarjeta'

    try:
        food = Payment_food()
        food.rut = rut
        food.num_cuenta = num_cuenta
        food.correo = correo
        food.product = selector
        food.pay = selector2
        food.save()
        status = True
    except:
        status = False
        input('ERROR EN LA IMPLEMENTACIÓN DEL OBJETO')
    return(status)
    
def delete_objects():
    print('Ingrese la id del objeto a eliminar')
    code = input()
    try:
        Payment_food.objects.all().filter(pk = code).delete()
        status = True
    except:
        print('ERROR AL ELIMINAR EL OBJETO CON LA ID INGRESADA')
        status = False
    return(status)
        

    
    

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
    
    def test_creation(self):
        self.assertTrue(add_objects())
    
    def test_delete(self):
        self.assertTrue(delete_objects())
