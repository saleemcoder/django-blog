from django.shortcuts import render, redirect
from django.contrib import messages, auth 
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentails')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        

        #checking password match
        if password == password2:
            #checking username from db
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # if login after register
                       # auth.login(request, user)
                       # messages.success(request, 'You are now logged in')
                       # return redirect('index')
                    user.save()
                    messages.success(request, 'Registration successful')
                    return redirect('login')
        else:
            messages.error(request, 'Pasword do not match')
            return redirect('register')

        
        # messages.error(request, 'Testing error message')
        # return redirect('register')
        # print('working')
        # return redirect('register')
    else:
        return render(request, 'accounts/register.html')

