from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('testpage/', views.testpage, name='testpage'),
    path('welcome/', views.welcome, name='welcome'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
    path('health/', views.health, name='health'),
    path('Asgm/', views.Asgm, name='Asgm'),
    path('ships/', views.ships, name='ships'),
    path('sign_up/', views.sign_up, name='sign_up'),

]
