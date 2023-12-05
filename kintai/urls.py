from django.urls import path
from . import views
from .views import KintaiList, KintaiDetail, KintaiCreate, KintaiUpdate, KintaiDelete, OvertimetargetList, OvertimetargetUpdate, BudgetList, BudgetUpdate


urlpatterns = [
    path('', views.topfunc, name='top'),
    path('kintai/', views.kintaitopfunc, name='kintaitop'),
    path('kintai/allmanagement/', views.allmanagementfunc, name='allmanagement'),
    path('kintai/overtime/', views.overtimefunc, name='overtime'),
    path('kintai/todaycost/', views.todaycostfunc, name='todaycost'),
    path('kintai/detailcost', views.detailcostfunc, name='detailcost'),
    path('kintai/edit/', KintaiList.as_view(), name='edit'),
    path('kintai/detail/<int:pk>', KintaiDetail.as_view(), name='detail'),
    path('kintai/create/', KintaiCreate.as_view(), name='create'),
    path('kintai/update/<int:pk>', KintaiUpdate.as_view(), name='update'),
    path('kintai/delete/<int:pk>', KintaiDelete.as_view(), name='delete'),
    path('kintai/overtimetarget/', OvertimetargetList.as_view(), name='overtimetarget'),
    path('kintai/updateovertimetarget/<int:pk>', OvertimetargetUpdate.as_view(), name='updateovertimetarget'),
    path('kintai/budget/', BudgetList.as_view(), name='budget'),
    path('kintai/updatebudget/<int:pk>', BudgetUpdate.as_view(), name='budgetupdate'),
    path('kintai/updatebudget/', BudgetUpdate.as_view(), name='budgetupdate'),
]