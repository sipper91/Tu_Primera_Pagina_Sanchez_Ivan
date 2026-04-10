from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_request, register, editar_perfil

urlpatterns = [
    path('login/', login_request, name='Login'),
    path('register/', register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='Logout'),
    path('perfil/editar/', editar_perfil, name='EditarPerfil'),
]
