from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


@admin.register(User)
class Custom_User_Admin(UserAdmin):
    model = User
    list_display = ("email", "is_active", "is_staff")
    list_filter = ("is_staff", "is_active")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("permissions", {"fields": ("is_staff",  "is_active",
         "is_superuser", "groups", "user_permissions")}),

    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": (
            "email", "password1", "password2", "is_staff", "is_active"), }),
    )
    search_fields = ("email" ,)
    
    
