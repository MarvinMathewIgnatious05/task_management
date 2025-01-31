from django.urls import path
from .views import login_page,registration
urlpatterns = [
    path("login_page",login_page,name="login_page"),
    path("",registration,name="registration_form"),
]