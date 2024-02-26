from django.urls import path, include
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("ajax/", include('frontend.ajax.urls')),
    
    path("terms-and-conditions/", tc, name="tc"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("cancellation-policy/", cancelation_policy, name="cancelation_policy"),
    path("about-us/", about_us, name="about_us"),
]