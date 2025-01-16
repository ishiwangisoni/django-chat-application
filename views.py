# messaging/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm

def index(request):
    return render(request, 'messaging/index.html')  # Ensure this template exists

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('chatroom')  # Redirect to chatroom after successful signup
    else:
        form = SignupForm()
    return render(request, 'messaging/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chatroom')  # Redirect to chatroom after successful login
        else:
            return render(request, 'messaging/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'messaging/login.html')

def chatroom(request):
    return render(request, 'messaging/chatroom.html')  # Ensure this template exists