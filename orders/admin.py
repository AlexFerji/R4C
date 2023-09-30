from django.contrib import admin

from .models import Order


class CustomOrder(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    model = Order
    list_display = ("customer", "robot_serial")


admin.site.register(Order, CustomOrder)


# Register your models here.
