from django.shortcuts import render, redirect

# Create your views here.

def loginfunc(request):
  return redirect(request, 'account/login.html')