from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import AboutMe


def about_me(request):
    about = AboutMe.objects.first()

    context = {
        "about_me": about
    }
    return render(request, 'about_me.html', context)
