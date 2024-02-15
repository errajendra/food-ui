from django.shortcuts import render
from django.http.response import JsonResponse
import requests



def submit_contact(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        email = data['email']
        mobile = data['mobile']
        subject = data['subject']
        message = data['message']
        contact = {
            "name" : name,
            "email" : email,
            "mobile" : mobile,
            "subject" : subject,
            "message" : message,
        }
        # url = ''
        # data = requests.post(url, json = contact)
        return JsonResponse({
            'status': 200,
            'message': "Form submitted successfully"
        })
    return JsonResponse({
        "status": 405,
        "message": "Not Allowed."
    })
