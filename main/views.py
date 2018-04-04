from django.shortcuts import render, redirect
from django.http import *
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.mail import BadHeaderError, EmailMessage
from .forms import ContactForm


def home(request):
    
    return render(request, 'home.html')


def places(request):
    locations = Location.objects.all()
    return render(request, 'places.html', {'locations': locations})


def profile(request, username):
    user = User.objects.get(username=username) 
    return render(request, 'profile.html',{'username':username})

def detail(request, location_id):
    location = Location.objects.get(id=location_id)
    return render(request, 'detail.html', {'location': location})


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pas']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'profile.html')
            else:
                messages.error(request,'username and password did not matched')

        except auth.ObjectNotExist:
            print("invalid user")

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')


def registration(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username =username,first_name=first_name,last_name=last_name,email=email,password=password)
            messages.success(request,'user registration successful')
            usr = auth.authenticate(username=username, password=password)
            auth.login(request, usr)
            return render(request, 'profile.html')
    
    else:
        form1 = UserCreationForm()
        return render(request, 'registration.html', {'form':form1})


def search(request):
    if request.method== 'POST':
        srch = request.POST['srh']

        if srch:
            match = Location.objects.filter(Q(name__istartswith=srch))


            if match:
                return render(request,'search.html', {'sr':match})
            else:
                messages.error(request,'No Results Found')
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'search.html')        



def feedback(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                    content,
                                    contact_email,
                                    ['nk26311996@gmail.com'], #change to your email
                                     reply_to=[contact_email],
                                   )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks/')
    return render(request, 'feedback.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')



def contact(request):
    return render(request, 'contact.html')





