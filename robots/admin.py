from django.contrib import admin


from .models import Robot


class CustomRobot(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    model = Robot
    list_display = ("serial", "model", "version", "created")


admin.site.register(Robot, CustomRobot)

# Register your models here.
