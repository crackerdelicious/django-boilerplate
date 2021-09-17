from django.urls import path

from apps.home import views as home_views

app_name = 'home'

urlpatterns = [
    path('', home_views.HomepageView.as_view(), name='homepage'),
]
