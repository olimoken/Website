from django.shortcuts import render
from .models import *

# Create your views here.

def Index(request):
    context={
        'zapal':Zapal.objects.all()
    }
    return render(request,"zapal.html",context)