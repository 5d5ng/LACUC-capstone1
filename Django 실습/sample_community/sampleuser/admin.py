from django.contrib import admin
from .models import Sampleuser
# Register your models here.


class SampleuserAdmin(admin.ModelAdmin):
    list_display = ('username','password')


admin.site.register(Sampleuser,SampleuserAdmin)