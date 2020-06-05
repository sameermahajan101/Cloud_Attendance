from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.


student = [
    {
        'moodleID': 15201577,
        'student': 'Prof. A',
        'year': 'BE',
        'time_logged': ''
    },

]


def home(request):
    context = {
        'student': Students.objects.all(),
    }
    return render(request, 'attendance/home.html', context)


def about(request):
    return render(request, 'attendance/about.html', {'title': 'About'})
