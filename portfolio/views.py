from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
import os
import requests
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def home(request:HttpRequest):
    if request.method == "GET":

        host = request.get_host() 

        url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

        payload = {
            'chat_id':CHAT_ID,
            'text': f"visted {host}"
        }
        requests.get(url,params=payload)

        return render(request=request, template_name="index.html")
    
    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        message = f"Name🫡: {name},\n Email📩: {email},\n Message🔤: {message}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
        "chat_id": CHAT_ID,
        "text": message
     }
        requests.post(url, json=payload)
        return render(request=request, template_name="index.html")
    
def components(requests:HttpRequest):
    return render(request=requests, template_name="components.html")

