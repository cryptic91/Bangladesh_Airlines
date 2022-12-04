from django.contrib import admin
from .models import Contact, Login, Signup, Ticket
# Register your models here.
admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(Signup)
admin.site.register(Ticket)
