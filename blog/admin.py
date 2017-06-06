from django.contrib import admin

# Register your models here.
from .models import Post


# admin.site.site_header = 'My administration_admin.py (2)'
admin.site.register(Post)