from django.shortcuts import render
from datetime import datetime

def index(request):
    n = datetime.now()
    return render(request, "newyear/index.html",{
        'newyear':n.month == 3 and n.day == 13
    })