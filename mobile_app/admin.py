from django.contrib import admin
from .models import AppUser,BankDetails,Transaction

admin.site.register(AppUser)
admin.site.register(BankDetails)
admin.site.register(Transaction)