from django.shortcuts import render


def home(request):
    context = {}
    if request.method == 'POST':
        numero = int(request.POST.get("numero"))
        result = numero**2
        context = {
            'numero': numero,
            'result': result,
        }
    return render(request, 'eqSysApp/home.html', context)
