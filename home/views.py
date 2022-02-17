from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from .models import Teacher
import random

# Create your views here.


def home(request):
    form = ContactForm()
    items = list(Teacher.objects.all()) 
    teachers = random.sample(items, 2)
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been sent")
            return redirect("home")

    context = {
        "form": form,
        "teachers" : teachers
    }

    return render(request, "home/index.html", context)


def about(request):
    return render(request, "home/about.html")


def teacher(request):
    teachers = Teacher.objects.all()
    context = {
        "teachers" : teachers
    }    
    return render(request, "home/teacher.html", context)
