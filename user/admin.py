from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from authentication.forms import UserForm, UserChangeForm
User = get_user_model()

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = UserChangeForm
    model = User
    # for changing / adding new info to fields
    add_fieldsets = (
        ('Personal Details', {'fields':('email', 'full_name', 'username', 'picture', 'password1', 'password2')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
        ('Optional',{'fields':('bio', 'website')}),
    )
    #shown fields to admin dashboard
    fieldsets = (
        ('Personal Details', {'fields':('email', 'full_name', 'username', 'picture')}),
        ('Permissions', {'fields':('is_staff', 'is_active')}),
          ('Optional',{'fields':('bio', 'website')}),
    )