from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


# contact page

def contact(request):
    return render(request, 'contact.html', {})

# about page

def about(request):
    return render(request, 'about.html', {})
