from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    if request.method == "POST":
        merk = request.POST['merk']
        year = request.POST['year']
        transmission = request.POST['transmission']
        nrg = request.POST['nrg']
        km = request.POST['km']
        price = request.POST['price']
        desc = request.POST['desc']
        email = request.POST['email']
        file = request.POST['file']
        naam = request.POST['naam']
        voornaam = request.POST['voornaam']
        gsm = request.POST['gsm']

        #groupement

        car_data = "Merk: " + merk + "\n" "Jaar: " + year + "\n""Transmissie: " + transmission + "\n""Brandstof: " + nrg + "\n""Kilometres: " + km + "\n""Prijs: " + price +"\n" "Description: " + desc + "\n""Email: " + email + "\n""Photos: " + file +"\n" "Naam: " + naam + "\n""Voornaam: " + voornaam + "\n""GSM nummer: " + gsm

        # send an email from form
        send_mail(
           'Taha, message from' + voornaam, # subject
            car_data,# message
            email,# from email
            ['sagingali.mamayev@gmail.com']# to email
        )

        return render(request, 'home.html', {'merk': merk, 'year': year,
                                             'transmission': transmission,
                                             'nrg': nrg, 'km': km, 'price': price,
                                             'desc': desc, 'email': email,
                                             'file': file, 'naam': naam,
                                             'voornaam': voornaam, 'gsm': gsm, })
    else:
        return render(request, 'home.html', {})




# contact page

def contact(request):
    return render(request, 'contact.html', {})


# about page

def about(request):
    return render(request, 'about.html', {})

# form data

def form_data(request):
    return render(request, 'form_data.html', {})