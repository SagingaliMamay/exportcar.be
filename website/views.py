from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import *


def home(request):
    return render(request, 'home.html', {})


# contact page

def contact(request):
    return render(request, 'contact.html', {})


# about page

def about(request):
    return render(request, 'about.html', {})


# form data

def form_data(request):
    form = Car_dataForm()

    data = {
        'form': form,

    }
    return render(request, 'upload.html', data)


# upload file
def upload(request):
    if request.method == 'POST':
        form = Car_dataForm(request.POST, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            subject = "New car is coming :"
            body = {
                'mark': form.cleaned_data['mark'],
                'year': form.cleaned_data['year'],
                'nrg': form.cleaned_data['nrg'],
                'transmission': form.cleaned_data['transmission'],
                'km': form.cleaned_data['km'],
                'price': form.cleaned_data['price'],
                'message': form.cleaned_data['description'],
                'email': form.cleaned_data['email'],
                'name': form.cleaned_data['name'],
                'tel': form.cleaned_data['tel'],
                'photo': form.cleaned_data['photo']

            }
            message = "\n".join(map(str, body.values()))
            send_mail(subject, message, 'exportcars111@gmail.com', ['exportcars111@gmail.com'])
            return render(request, 'thanks.html')

        else:
            form = Car_dataForm()

    form = Car_dataForm()
    data = {
        'form': form,
    }

    return render(request, 'upload.html', data)


def thanks(request):
    return render(request, 'thanks.html', {})
