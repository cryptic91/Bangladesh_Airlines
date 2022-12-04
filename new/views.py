from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact, Login, Signup, Ticket

# Create your views here.

def home (request):
    if request.method == 'POST':
        FlightNo = request.POST.get('FlightNo')
        Type = request.POST.get('Type')
        Origin = request.POST.get('Origin')
        Destination = request.POST.get('Destination')
        DepartureTime = request.POST.get('DepartureTime')
        ArrivalTime = request.POST.get('ArrivalTime')
        home = Ticket()
        home.FlightNo = FlightNo
        home.Type = Type
        home.Origin = Origin
        home.Destination = Destination
        home.DepartureTime = DepartureTime
        home.ArrivalTime = ArrivalTime
        home.save()
    return render(request, "home.html")

def about (request):
    return render(request, "about.html")

def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        # return HttpResponse('<h1> Thanks for Contact with us</h1>')
    return render(request, "contact.html")

def login (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # confirm = request.POST.get('confirm')
        login = Login()
        login.email = email
        login.password = password
        # login.confirm = confirm
        login.save()
    return render(request, "login.html")

def signup (request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        presentAdd = request.POST.get('presentAdd')
        parmanentAdd = request.POST.get('parmanentAdd')
        city = request.POST.get('city')
        # district = request.POST.get('district')
        code = request.POST.get('code')
        signup = Signup()
        signup.firstname = firstname
        signup.lastname = lastname
        signup.email = email
        signup.password = password
        signup.presentAdd = presentAdd
        signup.parmanentAdd = parmanentAdd
        signup.city = city
        signup.code = code
        # signup.district = district
        signup.save()
    return render(request, "signup.html")

# def showdata (request):
#     return render(request, "showdata.html")

def showdata(request):
    contacts = Contact.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Contact':contacts}
    return render(request,'showdata.html',data)

def logindata(request):
    logins = Login.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Login':logins}
    return render(request,'logindata.html',data)

def signupdata(request):
    signups = Signup.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Signup':signups}
    return render(request,'signupdata.html',data)

def ticket(request):
    tickets = Ticket.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Ticket':tickets}
    return render(request,'ticket.html',data)
