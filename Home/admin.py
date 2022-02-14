from django.contrib import admin

# Register your models here.
from .models import BlogModel,students

admin.site.register(BlogModel)
admin.site.register(students)


