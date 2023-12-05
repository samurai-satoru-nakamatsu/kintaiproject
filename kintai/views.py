from django.shortcuts import render
from django.utils import timezone
from .models import KintaiModel, Overtimetarget, Budget
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def topfunc(request):
  return render(request, 'top.html')

def kintaitopfunc(request):
  kintaidata = KintaiModel.objects.all()
  return render(request, 'kintaiapp/index.html', {'kintaidata':kintaidata})

def allmanagementfunc(request):
  kintaidata = KintaiModel.objects.all()
  return render(request, 'kintaiapp/allmanagement.html', {'kintaidata':kintaidata})

def overtimefunc(request):
  return render(request, 'kintaiapp/overtime.html')

def todaycostfunc(request):
  return render(request, 'kintaiapp/todaycost.html')

def detailcostfunc(request):
  return render(request, 'kintaiapp/detailcost.html')

class KintaiList(ListView):
  template_name = 'kintaiapp/edit.html'
  model = KintaiModel

class KintaiDetail(DetailView):
  template_name = 'kintaiapp/detail.html'
  model = KintaiModel

class KintaiCreate(CreateView):
  template_name = 'kintaiapp/create.html'
  model = KintaiModel
  fields = '__all__'
  success_url = reverse_lazy('list')

class KintaiUpdate(UpdateView):
  template_name = 'kintaiapp/update.html'
  model = KintaiModel
  fields = '__all__'
  success_url = reverse_lazy('list')

class KintaiDelete(DeleteView):
  template_name = 'kintaiapp/delete.html'
  model = KintaiModel
  success_url = reverse_lazy('list')



class OvertimetargetList(ListView):
  template_name = 'kintaiapp/overtimetarget.html'
  model = Overtimetarget

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_list'] = Overtimetarget.objects.all()
    return context

class OvertimetargetUpdate(UpdateView):
  template_name = 'kintaiapp/updateovertimetarget.html'
  model = Overtimetarget
  fields = '__all__'
  success_url = reverse_lazy('overtimetarget')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_list'] = Overtimetarget.objects.all()
    return context
  

class BudgetList(ListView):
  template_name = 'kintaiapp/budget.html'
  model = Budget

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['object_list'] = Budget.objects.all()
    return context

class BudgetUpdate(UpdateView):
  template_name = 'kintaiapp/updatebudget.html'
  model = Budget
  fields = '__all__'
  success_url = reverse_lazy('budget')


class OvertimealertList(ListView):
  model = KintaiModel
  template_name = 'kintaiapp/overtime.html'

  def get_queryset(self):
    queryset = super().get_queryset()
    overtimetarget = Overtimetarget.object.get(pk=1)

    for item in queryset:
      overtime = item.checkout - item.checkin - '9:00:00'
      if overtime > overtimetarget.name:
        item.overtimealert = '残業注意'
      else:
        item.overtimealert = '問題なし'
    return queryset

