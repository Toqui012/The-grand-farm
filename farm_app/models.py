from django.db import models
# Create your models here.

load_product = [
    # (1, 'Dapac Cerdas'),
    # (2, 'Aviplus'),
    # (3, 'Camperbroiler Granulado'),
    # (4, 'Conchilla'),
    # (5, 'Dapac Vacas'),
    # (6, 'Nantacor'),
    # (7, 'Guidolin Nutri Potros'),
    # (8, 'Red Kite'),

    ('Dapac Cerdas', 'Dapac Cerdas'),
    ('Aviplus', 'Aviplus'),
    ('Camperbroiler Granulado', 'Camperbroiler Granulado'),
    ('Conchilla', 'Conchilla'),
    ('Dapac Vacas', 'Dapac Vacas'),
    ('Nantacor', 'Nantacor'),
    ('Guidolin Nutri Potros', 'Guidolin Nutri Potros'),
    ('Red Kite', 'Red Kite'),
]

load_pay = [   
    ('Tarjeta', 'Tarjeta'),   
    ('Paypal', 'Paypal'),
]


class Payment_food(models.Model):

    rut = models.CharField(max_length=9, null=False)
    num_cuenta = models.BigIntegerField(null=False)
    correo = models.EmailField(max_length=255)
    # product = models.IntegerField(null=False, default=1, choices=load_product)
    product = models.CharField(max_length=255, null=False, choices=load_product, default='Dapac Cerdas')
    pay = models.CharField(max_length=255, null=False, choices=load_pay, default='Tarjeta')
    # pay = models.IntegerField(null=False, default=1, choices=load_pay)

    def __str__(self):
        return str(self.pk) #str castea a string :v 






