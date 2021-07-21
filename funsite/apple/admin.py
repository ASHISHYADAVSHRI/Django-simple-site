from django.contrib import admin
from .models import ToDo, Item
# Register your models here.
admin.site.register(ToDo)
admin.site.register(Item)