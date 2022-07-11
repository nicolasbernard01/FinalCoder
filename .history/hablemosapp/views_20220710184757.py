from distutils.log import info
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *

#def inicio(request):
#
#    debates = Debate.objects.all()
#
#    ctx = {'debates': debates}
#
#    return render(request,'hablemosapp/inicio.html', ctx)


def register_request(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username = username, password = password)

            if user is not None:

                login(request,user)
                return redirect('debate_list')

            else:

                return redirect('register')

        return render(request,'hablemosapp/register.html',{'form':form})

    form = UserRegisterForm()

    return render(request, 'hablemosapp/register.html', {'form': form})

def login_request(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:

                login(request, user)
                return redirect('debate_list')

            else: 

                return redirect('login')

        else:

            return redirect('login')
        
    form = AuthenticationForm()

    return render(request, r'hablemosapp/login.html', {'form': form})

def logout_request(request):

    logout(request)

    return redirect('debate_list')

class DebateList(ListView):

    model = Debate

    template_name = 'hablemosapp/debate_list.html'

class DebateDetail(DetailView):

    model = Debate

    template_name = 'hablemosapp/debate_detail.html'

class DebateCreate(CreateView):

    model = Debate

    success_url = '/debate/list'

    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]

class DebateUpdate(UpdateView):

    model = Debate

    success_url = '/debate/list'

    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]

class DebateDelete(DeleteView):

    model = Debate

    success_url = '/debate/list'

def editar_perfil(request):

    user= request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.nombre = info['nombre']
            user.apellido = info['apellido']
            user.email = info['email']

            user.save()

            return redirect('debate_list')

        else:
            
            form = UserEditForm(initial={'nombre':user.nombre, 'apellido':user.apellido,'email':user.email,'password1':user.password1, 'password2':user.password2})

        return render(request, 'hablemosapp/editar_perfil.html', {'form':form})

