from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.shortcuts import render
# Create your views here.


def home(request):
    
    req = requests.get("https://api.github.com/search/users?q=MediBoss")
    parsed_data = json.loads(req.text)
    result_array = parsed_data["items"]

    return render(request, 'templates/api/home.html')


