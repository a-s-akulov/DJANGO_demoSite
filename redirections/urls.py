from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r"^$", views.redirect_standart, kwargs={"redirectUrl": "polls:index"}, name="index"),
]