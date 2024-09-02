
import os
from django.http import HttpResponse, HttpResponseNotFound

class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host: str = request.get_host().split(':')[0]
        subdomain = host.replace(".", "_")
    
        if subdomain == 'accounts_nexaflow_co':
            request.urlconf = 'accounts.urls'
        elif subdomain == 'api_nexaflow_co':
            request.urlconf = 'api.urls'
        elif subdomain == 'admin_nexaflow_co':
            request.urlconf = 'admin_urls.urls'
        elif subdomain == 'www_nexaflow_co' or subdomain == 'nexaflow_co':
            pass
        else:
            request.urlconf = 'serve_site.urls'
        response = self.get_response(request)
        return response
