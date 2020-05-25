from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth import get_user_model
from data.models import Mainbar, Post
from .form import RegisterForm, LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


User = get_user_model()

def login(request):
    if request.POST:
        form = RegisterForm(request.POST)



        login = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(password=password, username=login)
        if user:
            auth.login(request, user)
        elif form.is_valid():

            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            u = User(username=login, password=password, email=email)
            u.save()
            auth.login(request, u)
            print(login, password, email)
            return redirect('/admin/')
        else:
            return redirect('/log/')
        return redirect('/shop/')
    else:
        response = csrf(request)
        response['bar'] = Mainbar.objects.all()
        response['mobar'] = Mainbar.objects.filter(mobile=True)
        response['form'] = RegisterForm()
        return render(request, 'form.html', response)

def out(request):
    data={
        'out_login': True
    }
    print(auth)
    auth.logout(request)
    print(auth)
    return JsonResponse(data)



def reg(request):
    if request.POST:
        form = RegisterForm(request.POST)
        login = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(password=password, username=login)
        data = {
            'is_taken': User.objects.filter(username__iexact=login).exists()
        }
        print("2")
        print(user)
        if user:
            auth.login(request, user)
            data = {
                'is_login': user.is_authenticated,
                'is_taken': User.objects.filter(username__iexact=login).exists()
            }
            print("2")
        elif form.is_valid():
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            NewUser = User(username=login, password=password, email=email)
            NewUser.save()
            auth.login(request, NewUser)
            data = {
                'is_login': NewUser.is_authenticated,
                'is_taken': User.objects.filter(username__iexact=login).exists()
            }
            print("3")
            return JsonResponse(data)
        else:
            print("4")
            return JsonResponse(data)
        print("5")
        return JsonResponse(data)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})