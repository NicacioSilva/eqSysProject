from django.shortcuts import render


def home(request):
    context = {}
    if request.method == 'POST':
        number = int(request.POST.get("number"))
        result = number**2
        context = {
            'number': number,
            'result': result,
        }
    return render(request, 'eqSysApp/home.html', context)
