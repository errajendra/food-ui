from django.shortcuts import render



def index(request):
    return render(request, 'frontend/index.html')


# Terms & Conditions
def tc(request):
    return render(request, 'frontend/tc.html')


# Privacy Policy
def privacy_policy(request):
    return render(request, 'frontend/privacy-policy.html')


# Cancelation Policy
def cancelation_policy(request):
    return render(request, 'frontend/cancelation-policy.html')


# About Us
def about_us(request):
    return render(request, 'frontend/about-us.html')
