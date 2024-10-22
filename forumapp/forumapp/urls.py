from django.contrib import admin
from django.urls import path, re_path
from boards import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
]