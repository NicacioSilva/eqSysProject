from django.shortcuts import render


def home(request):
    context = {}

    if request.method == 'POST':
        from eqSysApp.sympy.sympy import sys_manager
        context = sys_manager(request.POST.dict())

    return render(request, 'eqSysApp/home.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'eqSysApp/about.html', context)