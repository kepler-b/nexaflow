from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import os

def get_data_for_host(host: str, path: str = "/"):
    if os.path.exists(f'websites/{host}/{path}'):
        with open(f'websites/{host}/{path}', 'r') as file:
            content = file.read()
    else:
        with open(f'websites/{host}/index.html', 'r') as file:
            content = file.read()
    return content

def serve_app(request: HttpRequest):
    host = request.get_host().split(':')[0].replace(".", "_")

    return HttpResponse(get_data_for_host(host, request.path))
    