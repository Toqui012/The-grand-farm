from django.db import models
# Create your models here.

load_product = [
    (1, 'Dapac Cerdas'),
    (2, 'Aviplus'),
    (3, 'Camperbroiler Granulado'),
    (4, 'Conchilla'),
    (5, 'Dapac Vacas'),
    (6, 'Nantacor'),
    (7, 'Guidolin Nutri Potros'),
    (8, 'Red Kite'),
]

load_pay = [   
    (1, 'Tarjeta'),   
    (2, 'Paypal'),
]


class Payment_food(models.Model):

    rut = models.CharField(max_length=9, null=False)
    num_cuenta = models.BigIntegerField(null=False)
    correo = models.EmailField(max_length=255)
    product = models.IntegerField(null=False, default=1, choices=load_product)
    pay = models.IntegerField(null=False, default=1, choices=load_pay)

    def __str__(self):
        return str(self.pk) #str castea a string :v 






