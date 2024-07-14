from django.contrib import admin
from myapp.models import Contact_us
# Register your models here.
admin.site.site_header = "Cycle | Admin"

admin.site.register(Contact_us)