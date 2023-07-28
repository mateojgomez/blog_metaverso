from django.contrib import admin
from django.urls import path
from apps.usuarios import views
from .views import LoginUsuario
from django.contrib.auth import views as auth_views

app_name = 'apps.usuarios'


# Ceci en clase utiliza las views como clases
urlpatterns = [
    path('', views.RegistrarUsuario.as_view(), name='registration/registrar.html'),
    path('login/', LoginUsuario.as_view(), name= 'login'),
    path('logout/', views.LogoutUsuario.as_view(), name= 'logout'),
    path('registrarse/', views.RegistrarUsuario.as_view(), name = 'registrarse' ),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),   
            

]

# TODO continuar con la clase 7/7 desde el minuto 29
