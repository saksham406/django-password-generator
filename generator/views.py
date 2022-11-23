from django.shortcuts import render 
from django.http import HttpResponse 
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters=list('qwertyuioplkjhgfdsazxcvbnm')
    length = int(request.GET.get('length',12))
    
    if request.GET.get('uppercase'):
        characters.extend(list('qwertyuioplkjhgfdsazxcvbnm'.upper()))

    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()_+=][}{./<>"))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    gen_password = '' 
    for char in range(length):
        gen_password+=random.choice(characters)

    return render(request,'generator/password.html',{'password':gen_password}) 

def about(request):
    return render(request,'generator/about.html')