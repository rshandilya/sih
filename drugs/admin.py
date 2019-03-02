from django.contrib import admin
from .models import Drug, DrugCategory,DrugStock

# Register your models here.

admin.site.register(DrugCategory)
admin.site.register(Drug)
admin.site.register(DrugStock)