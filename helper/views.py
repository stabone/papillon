from django.shortcuts import render

# Create your views here.


def handler400(request):
    return render(request, 'helper/400_handler.html', {})


def handler403(request):
    return render(request, 'helper/403_handler.html', {})


def handler404(request):
    return render(request, 'helper/404_handler.html', {})


def handler500(request):
    return render(request, 'helper/500_handler.html', {})
