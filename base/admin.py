from django.contrib import admin
from .models import User
from .models import User,PasswordEntry,home

# Register your models here.
admin.site.register(User)
admin.site.register(PasswordEntry)
admin.site.register(home)
