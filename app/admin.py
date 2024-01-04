from django.contrib import admin
from . models import *
# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display = ('title','year','description')


admin.site.register(Movieinfo,movieAdmin)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(censorInfo)