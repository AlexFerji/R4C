from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer


class CustomCustomer(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    model = Customer
    # list_display = ("email")



admin.site.register(Customer, CustomCustomer)

# Register your models here.
