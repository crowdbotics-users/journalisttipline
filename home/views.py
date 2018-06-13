from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'datapunt-authorization-django', 'url': 'http://pypi.python.org/pypi/datapunt-authorization-django/0.2.18'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
