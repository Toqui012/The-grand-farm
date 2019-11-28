from django.urls import path
from . import views


urlpatterns = [
    path('payment_food_list/', views.payment_food_list, name='payment_food_list'),
    path('', views.index, name='index'),
    path('payment_food/', views.payment_food, name='payment_food'),
    path('payment_animal/',views.payment_animal, name='payment_animal'),
    path('payment_food_delete/<int:id>', views.payment_food_delete, name='payment_food_delete'),
    path('payment_food_update/<int:id>',views.payment_food_update, name='payment_food_update'),
    path('register_user/',views.register_user, name= 'register_user'),
    # path('payment_food_delete/',views.payment_food_delete, name="payment_food_delete")
]