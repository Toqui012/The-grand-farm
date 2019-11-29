from django.shortcuts import render
from .models import Payment_food #punto significa directorio actual
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here. 
def payment_food_list(request):
    list = Payment_food.objects.all()
    status = ''
    if request.method == 'POST':
        try:
            status = 'SEARCH'
            rut_busca = request.POST.get('buscar_rut')
            if Payment_food.objects.all().filter(rut = rut_busca).exists() == True:
                list = Payment_food.objects.filter(rut = rut_busca)
            else:
                if Payment_food.objects.all().filter(pk = rut_busca).exists() == True:
                    list = Payment_food.objects.filter(pk = rut_busca)
                else:
                    list = Payment_food.objects.all()
        except:
            status = 'NOTSEARCH'
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

def payment_food_update(request,id):
    status = ''
    producto = ['Dapac Cerdas','Aviplus','Camperbroiler Granulado','Conchilla','Dapac Vacas','Nantacor','Guidolin Nutri Potros','Red Kite']
    formaPago = ['Tarjeta','Paypal']
    pedido = Payment_food.objects.get(pk = id)
    if request.method == 'POST':
        try:
            pedido = Payment_food.objects.get(pk = id)
            pedido.rut = request.POST.get('txtRut') if request.POST.get('txtRut') != None else pedido.rut
            pedido.num_cuenta = request.POST.get('txtNumTarjeta') if request.POST.get('txtNumTarjeta') != None else pedido.num_cuenta
            pedido.correo = request.POST.get('txtCorreo') if request.POST.get('txtCorreo') != None else pedido.correo
            pedido.product = request.POST.get('txtProducto') if request.POST.get('txtProducto') != None else pedido.product
            pedido.pay = request.POST.get('txtFormaPago') if request.POST.get('txtFormaPago') != None else pedido.pay
            pedido.save()
            status = 'OK'
        except: 
            status = 'ERROR'
    variables = {'status': status,
                 'producto': producto,
                 'formaPago': formaPago,
                 'pedido': pedido}
    return render(request,'farm_app/payment_food_update.html', variables)

def register_user(request):
    status = ''
    if request.method == 'POST':
        user = User()
        try:
            user = User.objects.create_user(username = request.POST.get('txtRut'),
            password = request.POST.get('txtPass'),
            email = request.POST.get('txtCorreo'),
            last_name = request.POST.get('txtApellido'),
            first_name = request.POST.get('txtNombre'))
        except:
            status = 'ERROR'
            return render(request,'farm_app/register_user.html', {'status' : status})
        user.save()
        status= 'OK'
    return render(request,'farm_app/register_user.html', {'status' : status})

def login_view(request):
    status = ''
    if request.method == 'POST':
        username = request.POST.get('txtRutLogin')
        password = request.POST.get('txtPassLogin')
        user = authenticate(request, username = username, password = password )
        if user:
            login(request, user)
            status = 'OK'
            return HttpResponseRedirect(reverse('index'))
        else:
            status = 'ERROR'
            messages.error(request,'Error al iniciar sesion :c ')
    variables = {'status':status}
    return render(request,'farm_app/login_view.html', variables)

@login_required(login_url = 'login')
def logout_view(request):
    logout(request)
    return redirect('login')


