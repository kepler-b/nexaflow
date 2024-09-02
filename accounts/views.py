from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json

client_details = {
    "client_id": "1234567890",
    "client_secret": "3b3f9e2f4dcaefc2bcde54dd1f4cdd7e4fb346b2c9df69729ce9315b8bd12cb8",
}

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html', {"request": request})

def signin(request):
    if request.method == 'POST':
        print(request.POST)
    
    client_id = request.GET.get('client_id')
    redirect_uri = request.GET.get('redirect_uri')
    response_type = request.GET.get('response_type')
    print(client_id, redirect_uri, response_type)

    if client_id == client_details["client_id"]:
        import random
        import string
        import urllib.parse

        # Generate a random code
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        client_details["code"] = code
        # Construct the redirect URL with the code
        redirect_url = f"{redirect_uri}?code={code}"

        # Encode the URL to ensure it's properly formatted
        encoded_redirect_url = urllib.parse.quote(redirect_url, safe=':/?=&')

        # Redirect to the constructed URL
        from django.shortcuts import redirect
        return redirect(encoded_redirect_url)
    
    if not all([client_id, redirect_uri, response_type]):
        return HttpResponse("Missing required parameters")
    
    context = {
        "request": request,
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": response_type
    }
    
    return render(request, 'accounts/signin.html', context)

@csrf_exempt
def authorize(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        code = data.get('code')
        client_id = data.get('client_id')
        client_secret = data.get('client_secret')
        if code == client_details["code"] and client_id == client_details["client_id"] and client_secret == client_details["client_secret"]:
            return JsonResponse({"message": "Authorized","access_token": "1234567890"})
        else:
            return HttpResponse("Invalid code")


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})

def signup(request):
    return render(request, 'accounts/signup.html', {"request": request})

def forgot_password(request):
    return render(request, 'accounts/forgot_password.html', {"request": request})

def reset_password(request):
    return render(request, 'accounts/reset_password.html', {"request": request})

def change_password(request):
    return render(request, 'accounts/change_password.html', {"request": request})