from django.contrib import admin
from .models import BlogList, Registration

# Register your models here.
admin.site.register(Registration)
admin.site.register(BlogList)

