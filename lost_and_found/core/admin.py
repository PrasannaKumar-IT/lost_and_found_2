from django.contrib import admin
from .models import ClassRoom, StudentRegistration, CustomUser, Item,Course
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('course', 'year')
    search_fields = ('course',)

@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('reg_no', 'student_name', 'classroom')
    list_filter = ('classroom',)
    search_fields = ('reg_no', 'student_name')

@admin.action(description="Mark selected items as Returned")
def mark_as_returned(modeladmin, request, queryset):
    queryset.update(status="Returned")
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_type', 'status', 'reported_by', 'date_reported')
    list_filter = ('status', 'item_type', 'date_reported')
    search_fields = ('title', 'description', 'reported_by__username')
    list_editable = ('status',)
    actions = [mark_as_returned]
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50"/>', obj.image.url)
        return "No Image"

admin.site.register(Course)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'reg_no', 'classroom', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_header = "Lost & Found Admin"
admin.site.site_title = "Lost & Found"
admin.site.index_title = "Welcome to Lost & Found Dashboard"
