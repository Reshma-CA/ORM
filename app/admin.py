from django.contrib import admin
from . models import Movieinfo
# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display = ('title','year','description')


admin.site.register(Movieinfo,movieAdmin)