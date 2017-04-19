from django.shortcuts import render

# Create your views here.
def roupas_list(request):
    return render(request, 'aluguelroupas/roupas_list.html',{})
