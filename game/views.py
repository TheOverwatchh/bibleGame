from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def gameLobby(request):
    return render(request, 'lobby.html')

def gameRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # try to authenticate, if true, return to an error page
        check = authenticate(username=username, password=password)
        if check: 
            return redirect('errorPage', status=23)
        u = User.objects.create_user(username, email, password)
        login(request, user=u)
        return redirect('gameLobby')


def gameLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        check = authenticate(username=username, password=password)
        if check:
            login(request, check)
            return redirect('gameLobby') 
        return redirect('errorPage', status=22)

def logout_dj(request):
       logout(request)
       return redirect('gameLobby') 

def errorPage(request, status):
    if status == 22:
        error = 'User not found.'
    else: 
        error = 'This username is already taken.'    
    return render(request, 'error.html', {
        'error': error
    })