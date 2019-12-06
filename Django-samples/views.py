from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("""
        <h1>Bienvenu sur le blog de m2i!</>
        <p>Le framework Django est chouette!</p>
    """)
