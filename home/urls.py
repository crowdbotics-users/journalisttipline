from django.conf.urls import url    
from .views import home, ProfileUpdate

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^accounts/profile_update/(?P<pk>[\w-]+)', ProfileUpdate.as_view(), name="account_profile_update"),
]   
