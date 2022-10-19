from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def logIn(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        form = AuthenticationForm(data=request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('home')
            else:
                form = AuthenticationForm(data = request.POST)
                return render(request, 'login.html', {'form': form, 'error': True})
        return render(request, 'login.html', {'form':form})

def home(request):
    return render(request, 'home.html')

def logOut(request):
    if(request.method == 'POST'):
        logout(request)
        return redirect('logIn')