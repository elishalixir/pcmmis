from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('testpage/', views.testpage, name='testpage'),
    path('welcome/', views.welcome, name='welcome'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
    path('health/', views.health, name='health'),
    path('cement/', views.cement_sector, name='cement'),
    path('mercury_products/', views.mercury_added_products, name='mercury_products'),
    path('energy/', views.energy_fuel, name='energy'),
    path('Asgm/', views.Asgm, name='Asgm'),
    path('sign_up/', views.sign_up, name='sign_up'),

]
