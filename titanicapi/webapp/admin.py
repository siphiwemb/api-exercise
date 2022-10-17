from django.contrib import admin
from .models import Titanic

# Register your models here.

@admin.register(Titanic)
class Titanic_tbl(admin.ModelAdmin):
    list_display = ('uuid', 'survived', 'passenger_class', 'name', 'sex', 'age', 
    'siblings_spousesaboard', 'parents_childrenaboard', 'fare')