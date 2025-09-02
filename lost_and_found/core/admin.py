from django.contrib import admin
from .models import ClassRoom, StudentRegistration, CustomUser, Item,Course
from django.contrib.auth.admin import UserAdmin

admin.site.register(ClassRoom)
admin.site.register(StudentRegistration)
admin.site.register(Item)
admin.site.register(Course)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'reg_no', 'classroom', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
