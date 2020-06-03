from django.conf.urls import url
from .views import HomePageView, AboutPage

urlpatterns = [
    url(r'^about/', AboutPage.as_view(), name = 'about'),
    url(r'', HomePageView.as_view(), name = 'home'),
    
]
