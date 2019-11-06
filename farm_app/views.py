from django.shortcuts import render
from .models import Payment_food #punto significa directorio actual

# Create your views here. 
def payment_food_list(request):
    list = Payment_food.objects.all()
    status = ''
    variables = {'status': status,
                  'list': list}
    return render(request,'farm_app/payment_food_list.html', variables)

def payment_food(request):
    status = 'NO_CONTENT'
    if request.method == 'POST':
        try:
            food = Payment_food()
            food.rut = request.POST.get('rut')
            food.num_cuenta = request.POST.get('num_cuenta')
            food.correo = request.POST.get('correo')
            food.product = request.POST.get('selector')
            food.pay = request.POST.get('selector2')
            food.save()
            status = 'OK'
        except :
            status = 'ERROR'
    return render(request, 'farm_app/comida.html', {'status': status})


def payment_animal(request):
    return render(request,'farm_app/animal.html',{})

def index(request):
    return render(request,'farm_app/index.html',{})

def payment_food_delete(request,id):
    # return render(request,'farm_app/payment_food_delete.html',{})
    status = 'NO_CONTENT'
    list = Payment_food.objects.all()
    Payment_food.objects.get(pk = id).delete()
    status = 'DELETED'
    variables = {'status': status,
                'list': list}
    return render(request, 'farm_app/payment_food_list.html', variables)


        