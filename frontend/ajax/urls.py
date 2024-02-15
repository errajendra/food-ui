from django.urls import path
from .views import *


urlpatterns = [
    path("submit-contact/", submit_contact, name="submit_contact"),
]