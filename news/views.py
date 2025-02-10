from django.shortcuts import render
from django.http import JsonResponse
import json


def home(request):
    import requests
    import json
    news_api_request=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9dd3daffaa0a4a7bb8b7e4485829f3bd")
    api=json.loads(news_api_request.content)
    return render(request,'index.html',{'api':api})
