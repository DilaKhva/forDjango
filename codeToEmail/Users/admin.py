# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
#
# from .models import *
#
# # Register your models here.
#
# admin.site.register([CustomUser, EmailCode])
#
# @admin.register(EmailCode)
# class EmailCodeAdmin(admin.ModelAdmin):
#     list_display = ('user', 'code', 'created_at')


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EmailCode

# Register CustomUser with default UserAdmin
admin.site.register(CustomUser, UserAdmin)

# Register EmailCode with a simple ModelAdmin
# @admin.register(EmailCode)
# class EmailCodeAdmin(admin.ModelAdmin):
#     list_display = ('user', 'code', 'created_at')
