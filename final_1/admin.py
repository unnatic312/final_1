from django.contrib import admin
from .models import msg, users


# Register your models here. It will show table in website admin control page
admin.site.register(msg)
admin.site.register(users)