from django.shortcuts import render


def home(request):
    context = {}
    if request.method == 'POST':
        a1 = float(request.POST.get("a1"))
        b1 = float(request.POST.get("b1"))
        c1 = float(request.POST.get("c1"))
        a2 = float(request.POST.get("a2"))
        b2 = float(request.POST.get("b2"))
        c2 = float(request.POST.get("c2"))
        from eqSysApp.sympy.sympy import sys_2x2
        context = sys_2x2(a1, b1, c1, a2, b2, c2)
    return render(request, 'eqSysApp/home.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'eqSysApp/about.html', context)