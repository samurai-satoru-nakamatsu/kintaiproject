from django.urls import path
from . import views

urlpatterns = [
    path('', views.topfunc, name='top'),
    path('kintai/', views.kintaitopfunc, name='kintaitop'),
    path('kintai/allmanagement/', views.allmanagementfunc, name='allmanagement'),
    path('kintai/overtime/', views.overtimefunc, name='overtime'),
    path('kintai/todaycost/', views.todaycostfunc, name='todaycost'),
    path('kintai/laborstandardact', views.laborstandardact, name='laborstandardact'),
    path('kintai/detailcost', views.detailcostfunc, name='detailcost'),
]