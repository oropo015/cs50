from django.shortcuts import render
from django import forms

class add_task(forms.Form):
    form = forms.CharField(label="Enter new task")

tasks = ['Blue', 'Green', 'Red']

def index(request):
    return render(request, 'task/index.html', {
        'tasks':tasks
    })

def add(request):
    return render(request, 'task/add.html', {
        'form':add_task()
    })