from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.shortcuts import render
# Create your views here.



def home(request):

    context = {}
    return render(request, 'api/home.html', {})

def search(request):
    
    query = request.POST.get('user_query', 'No user_query found.')
    req = requests.get("https://api.github.com/search/users?q={}".format(query))
    parsed_data = json.loads(req.text)
    result_array = parsed_data["items"]

    return HttpResponse(result_array)


