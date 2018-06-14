from django.shortcuts import render
from django.views.generic import UpdateView
from django.contrib.auth.models import User
# Create your views here.

from home.models import CustomText, HomePage
from .forms import ProfileForm


def home(request):
    packages = [
	{'name':'django-oscar', 'url': 'http://pypi.python.org/pypi/django-oscar/1.5.1'},
	{'name':'django-oscar', 'url': 'http://pypi.python.org/pypi/django-oscar/1.5.1'},
	{'name':'django-social-auth', 'url': 'http://pypi.python.org/pypi/django-social-auth/0.7.28'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
	{'name':'django-guardian', 'url': 'http://pypi.python.org/pypi/django-guardian/1.4.9'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)


class ProfileUpdate(UpdateView):
    template_name = "account/profile_update.html"
    form_class = ProfileForm
    success_url = "/"
    model = User