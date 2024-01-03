from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',Movie,name = 'register-page'),
    path('list/',data_view,name = 'list'),
    path('edit/<id>',edit,name = 'edit'),
    path('delete/<id>',delete,name = 'delete'),
   

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)