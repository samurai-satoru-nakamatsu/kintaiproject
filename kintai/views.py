from django.shortcuts import render

# Create your views here.

def topfunc(request):
  return render(request, 'top.html')

def kintaitopfunc(request):
  return render(request, 'kintaiapp/index.html')

def allmanagementfunc(request):
  return render(request, 'kintaiapp/allmanagement.html')

def overtimefunc(request):
  return render(request, 'kintaiapp/overtime.html')

def todaycostfunc(request):
  return render(request, 'kintaiapp/todaycost.html')

def laborstandardact(request):
  return render(request, 'kintaiapp/laborstandardact.html')