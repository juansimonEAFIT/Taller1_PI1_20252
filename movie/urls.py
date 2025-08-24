from django.urls import path
from .views import home, about, statistics_view,signup

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('statistics/', statistics_view, name='statistics'),
    path('signup/', signup, name='signup'),
]