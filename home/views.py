from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'django-profiling-dashboard', 'url': 'http://pypi.python.org/pypi/django-profiling-dashboard/0.2'},
	{'name':'custom-user-roles', 'url': 'http://pypi.python.org/pypi/custom-user-roles/1.1.0'},
	{'name':'datapunt-authorization-django', 'url': 'http://pypi.python.org/pypi/datapunt-authorization-django/0.2.18'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
