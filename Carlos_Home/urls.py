from django.conf.urls import url
from .views import home, about, ContactView

urlpatterns = [
    url(r'^$', home, name= "home"),
    url(r'^about/$',about, name = "about_view"),
    url(r'^contacto$', ContactView.as_view(), name = "contacto")
]
