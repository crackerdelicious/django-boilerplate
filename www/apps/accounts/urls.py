from django.urls import path

from apps.accounts import views as app_views

app_name = 'accounts'

urlpatterns = [
    path('login/', app_views.AccountsLoginView.as_view(), name='login'),
    path('logout/', app_views.AccountsLogoutView.as_view(), name='logout'),
    path('profile/', app_views.AccountsProfileView.as_view(), name='profile'),
]
