from django.conf.urls import url
from .views import home, about, RegisterUser, ContactView

urlpatterns = [
    url(r'^$', home, name= "home"),
    url(r'^about/$',about, name = "about_view"),
    url(r'^registrar/$', RegisterUser.as_view(), name = "register_view"),
    url(r'^contacto$', ContactView.as_view(), name = "contacto")
]
