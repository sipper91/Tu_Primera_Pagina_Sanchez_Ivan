from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm
from .models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect("inicio") 
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        
        form = UserEditForm(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            form.save()
            
            
            imagen_nueva = request.FILES.get('imagen')
            if imagen_nueva:
                
                Avatar.objects.filter(user=usuario).delete()
                avatar = Avatar(user=usuario, imagen=imagen_nueva)
                avatar.save()
                
            return redirect('inicio')
    else:
        
        form = UserEditForm(instance=usuario)
        
    return render(request, "accounts/editar_perfil.html", {"form": form})
