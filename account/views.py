from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    
    return render(request,"account/signup.html")


def handlelogin(request):
    
    return render(request,"account/login.html")


def handlelogout(request):
    return redirect('/account/login')