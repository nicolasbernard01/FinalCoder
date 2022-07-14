from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Debate, Avatar, Comentario,User
from .forms import AvatarForm, UserEditForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

@login_required
def logout_request(request):

    logout(request)

    return redirect('debate_list')

class DebateList(ListView):

    model = Debate

    template_name = 'hablemosapp/debate_list.html'

def leer_debate(request, debate_id):

    debate = Debate.objects.get(id=debate_id)

    ctx = {'debate':debate}

    return render(request, r'hablemosapp/leer_debate.html', ctx)

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

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.email = info['email']

            user.save()

            

            return redirect('debate_list')

        else:

            messages.error(request, r"Error al actualizar su perfil, verifique las contraseñas")

            form = UserEditForm(initial = {'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email})

            return redirect('editar_perfil')

    else:

        form = UserEditForm(initial = {'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email})   

        return render(request, r'hablemosapp/editar_perfil.html', {'form':form})

@login_required
def user_avatar(request):

    if request.method == 'POST':

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username)

            avatar = Avatar(usuario=user, imagen = form.cleaned_data['imagen'])

            avatar.save()

            return redirect('debate_list')

    else:

        form = AvatarForm()

    return render(request,r'hablemosapp/user_avatar.html', {'form':form})
