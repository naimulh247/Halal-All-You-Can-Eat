from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    # return render(request, 'home.html', {})
    return redirect(resturant_home)

@login_required(login_url='/resturant/sign_in/')
def resturant_home(request):
    return render(request, 'resturant/home.html', {})
