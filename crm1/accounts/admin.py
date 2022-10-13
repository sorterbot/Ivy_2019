from django.contrib import admin

# Register your models here.
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Customer, AuthorAdmin)
admin.site.register(Product, AuthorAdmin)
admin.site.register(Order, AuthorAdmin)
admin.site.register(Tag, AuthorAdmin)