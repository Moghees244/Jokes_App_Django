# jokes_app/views.py
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
import requests

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('joke')
    else:
        form = UserCreationForm()
    return render(request, 'jokes_app/registration.html', {'form': form})

@login_required
def joke(request):
    joke = request.session.get('joke')
    if request.method == 'POST' or not joke:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke_data = response.json()
        joke = f"{joke_data.get('setup')} - {joke_data.get('punchline')}"
        request.session['joke'] = joke
    return render(request, 'jokes_app/jokes.html', {'joke': joke})

def logout_view(request):
    logout(request)
    request.session.flush()  # Clears out the session data
    return redirect(settings.LOGOUT_REDIRECT_URL)