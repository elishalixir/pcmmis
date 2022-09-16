from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, asgm_education_health, Mercury_products, energy, cement, EnvironmentalHealth, NewRegistration, ArtisanalAndSmallScaleGoldMining, ArtisanalAndSmallScaleGoldMining2
from django.forms import ValidationError
from .models import ASGMElisha
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError


# Create your views here.


@login_required(login_url='/login')
def home(request):
    return HttpResponse('Test PAGE')


def sign_up(request):
    if request.method == 'POST':
        form = NewRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/health')
    else:
        form = NewRegistration()
        return render(request, 'registration/sign_up.html', {'form': form})

    return render(request, 'registration/login.html')


@login_required(login_url='/login')
def welcome(request):
    return render(request, 'dpcmmis/welcome.html')


@login_required(login_url='/login')
def testpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'dpcmmis/feedback.html')
    else:
        form = ContactForm()
        return render(request, 'dpcmmis/contact.html', {"form": form})


@login_required(login_url='/login')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Enquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect("feedback")
    else:
        form = ContactForm()
        return render(request, "dpcmmis/contact.html", {'form': form})


@login_required(login_url='/login')
def feedback(request):
    return render(request, "dpcmmis/feedback.html")


@login_required(login_url='/login')
def Asgm(request):
    if request.method == "POST":
        form = ArtisanalAndSmallScaleGoldMining(request.POST)
        one = request.POST['one']
        two = request.POST['two']
        three = request.POST['three']
        four = request.POST['four']
        five = request.POST['five']
        six = request.POST['six']
        seven = request.POST['seven']
        eight = request.POST['eight']
        nine = request.POST['nine']
        ten = request.POST['ten']
        eleven = request.POST['eleven']
        twelve = request.POST['twelve']
        if form.is_valid():
            # ASGMElisha = Asgm( one=one, two=two, three=three, four=four, five=five, six=six, seven=seven, eight=eight, nine=nine, ten=ten)
            form.save()
            return render(request, 'dpcmmis/feedback.html', {'one': one, 'two': two, 'three': three, 'four': four,
                                                             'five': five, 'six': six, 'seven': seven, 'eight': eight,
                                                             'nine': nine, 'ten': ten, 'eleven': eleven, 'twelve': twelve})
    else:
    # trial
        if request.method == "POST":
            form2 = ArtisanalAndSmallScaleGoldMining2(request.POST)
            one = request.POST['one']
            two = request.POST['two']
            three = request.POST['three']
            four = request.POST['four']
            five = request.POST['five']
            six = request.POST['six']
            seven = request.POST['seven']
            eight = request.POST['eight']
            nine = request.POST['nine']
            ten = request.POST['ten']
            eleven = request.POST['eleven']
            twelve = request.POST['twelve']
            thirteen = request.POST['thirteen']
            fourteen = request.POST['fourteen']
            fifteen = request.POST['fifteen']
            sixteen = request.POST['sixteen']
            seventeen = request.POST['seventeen']
            eighteen = request.POST['eighteen']
            nineteen = request.POST['nineteen']
            twenty = request.POST['twenty']
            twenty_one = request.POST['twenty_one']
            if form2.is_valid():
                form2.save()
                return render(request, 'dpcmmis/feedback.html', {'one': one, 'two': two, 'three': three, 'four': four,
                                                             'five': five, 'six': six, 'seven': seven, 'eight': eight,
                                                             'nine': nine, 'ten': ten, 'eleven': eleven, 'twelve': twelve,
                                                                 'thirteen': thirteen, 'fourteen': fourteen, 'fifteen': fifteen,
                                                                 'sixteen':sixteen, 'seventeen': seventeen, 'eighteen': eighteen,
                                                                 'nineteen': nineteen, 'twenty': twenty, 'twenty_one': twenty_one})
        else:
            if request.method == "POST":
                form3 = asgm_education_health(request.POST)
                one = request.POST['one']
                two = request.POST['two']
                three = request.POST['three']
                if form3.is_valid():
                    form3.save()
                    return render(request, 'dpcmmis/feedback.html', {'one': one, 'two': two, 'three': three})
            else:
                form = ArtisanalAndSmallScaleGoldMining()
                form2 = ArtisanalAndSmallScaleGoldMining2()
                form3 = asgm_education_health()
                return render(request, 'dpcmmis/asgm.html', {'form': form, 'form2': form2, 'form3': form3})

@login_required(login_url='/login')
def health(request):
    if request.method == "POST":
        form = EnvironmentalHealth(request.POST)
        if form.is_valid():
            return render(request, 'dpcmmis/feedback.html')
    else:
        form = EnvironmentalHealth()
        return render(request, 'dpcmmis/health.html', {'form': form})

def cement_sector(request):
    if request.method == "POST":
        form = cement(request.POST)
        if form.is_valid():
            return render(request, 'dpcmmis/feedback.html')

    else:
        if request.method == "POST":
            form2 = cement(request.POST)
            if form2.is_valid():
                one = request.POST['one']
                two = request.POST['two']
                three = request.POST['three']
                four = request.POST['four']
                return render(request,
                              'dpcmmis/feedback.html', {'one': one, 'two': two, 'three': three, 'four': four})
        else:
            form = cement()
            form2 = cement()
            return render(request, 'dpcmmis/cement.html', {'form': form, 'form2': form2})


def energy_fuel(request):
    if request.method == "POST":
        form = energy(request.POST)
        if form.is_valid():
            return render(request, 'dpcmmis/feedback.html')

    else:
        if request.method == "POST":
            form2 = energy(request.POST)
            if form2.is_valid():
                one = request.POST['one']
                two = request.POST['two']
                three = request.POST['three']
                four = request.POST['four']
                return render(request,
                              'dpcmmis/feedback.html', {'one': one, 'two': two, 'three': three})
        else:
            form = energy()
            form2 = energy()
            return render(request, 'dpcmmis/energy.html', {'form': form, 'form2': form2})

def mercury_added_products(request):
    if request.method == "POST":
        form = Mercury_products(request.POST)
        if form.is_valid():
            return render(request, 'dpcmmis/feedback.html')

    else:
        if request.method == "POST":
            form2 = Mercury_products(request.POST)
            if form2.is_valid():
                one = request.POST['one']
                two = request.POST['two']
                three = request.POST['three']
                four = request.POST['four']
                return render(request,
                              'dpcmmis/feedback.html', {'one': one, 'two': two, 'three': three})
        else:
            form = Mercury_products()
            form2 = Mercury_products()
            return render(request, 'dpcmmis/mercury_products.html', {'form': form, 'form2': form2})