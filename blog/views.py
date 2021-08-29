from django.shortcuts import render
from blog_settings.models import Setting


# header code behind
def header(request, *args, **kwargs):
    context = {
        'settings': Setting.objects.first()
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request):
    context = {
        'settings': Setting.objects.first()
    }
    return render(request, 'shared/Footer.html', context)
