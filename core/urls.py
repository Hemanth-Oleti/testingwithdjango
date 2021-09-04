import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from blog import views
#from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('__debug__/', include(debug_toolbar.urls)),
    #path('', views.index),
]

