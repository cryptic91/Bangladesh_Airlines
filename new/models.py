from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    message = models.TextField(max_length=500,null=True)

    def __str__(self):
        return self.name

class Login(models.Model):
    email = models.EmailField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    # confirm = models.TextField(max_length=50,null=True)

    def __str__(self):
        return self.email

class Signup(models.Model):
    firstname = models.CharField(max_length=30,null=True)
    lastname = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=100,null=True)
    password = models.TextField(max_length=30,null=True)
    presentAdd = models.TextField(max_length=150,null=True)
    parmanentAdd = models.TextField(max_length=150,null=True)
    city = models.TextField(max_length=50,null=True)
    code = models.IntegerField(max_length=50,null=True)
    # district = models.TextChoices

    def __str__(self):
        return self.firstname

class Ticket(models.Model):
    FlightNo = models.TextChoices('FlightNo', 'BA3882 BA3871 BA3333')
    Type = models.TextChoices('Type', 'A B C')
    Origin = models.TextChoices('Origin', 'Dhaka Chattogram Khulna')
    Destination = models.TextChoices('Destination', 'Dhaka Chattogram Khulna')
    DepartureTime = models.TextChoices('DepartureTime', '7am 9am 11am 1pm 3pm 5pm 7pm')
    ArrivalTime = models.TextChoices('ArrivalTime', '7am 9am 11am 1pm 3pm 5pm 7pm')

    def __str__(self):
        return self.FlightNo
