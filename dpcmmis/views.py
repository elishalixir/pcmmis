from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, EnvironmentalHealth, NewRegistration, Ship, ArtisanalAndSmallScaleGoldMining, ArtisanalAndSmallScaleGoldMining2
from django.forms import ValidationError
from .models import ASGMElisha
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def ships(self):
    shipping = self.clean_data.get('shipping')
    if shipping:
        msg = Ship.ValidationError("This field is required.")
        self.add_error('shipping_destination', msg)
    else:
        self.clean_data['shipping_destination'] = ''
    return self.clean_data


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
        if form.is_valid():
            # ASGMElisha = Asgm( one=one, two=two, three=three, four=four, five=five, six=six, seven=seven, eight=eight, nine=nine, ten=ten)
            form.save()
            return render(request, 'dpcmmis/feedback.html', {'one': one, 'two': two, 'three': three, 'four': four})
    else:
    # trial
        if request.method == "POST":
            form2 = ArtisanalAndSmallScaleGoldMining2(request.POST)
            five = request.POST['five']
            six = request.POST['six']
            seven = request.POST['seven']
            eight = request.POST['eight']
            if form2.is_valid():
                # ASGMElisha = Asgm( one=one, two=two, three=three, four=four, five=five, six=six, seven=seven, eight=eight, nine=nine, ten=ten)
                form2.save()
                return render(request, 'dpcmmis/feedback.html', {'five': five, 'six': six, 'seven': seven, 'eight': eight})
        else:
            form = ArtisanalAndSmallScaleGoldMining()
            form2 = ArtisanalAndSmallScaleGoldMining2()
            return render(request, 'dpcmmis/asgm.html', {'form': form, 'form2': form2})



@login_required(login_url='/login')
def health(request):
    if request.method == "POST":
        form = EnvironmentalHealth(request.POST)
        if form.is_valid():
            return render(request, 'dpcmmis/feedback.html')
    else:
        form = EnvironmentalHealth()
        return render(request, 'dpcmmis/health.html', {'form': form})
