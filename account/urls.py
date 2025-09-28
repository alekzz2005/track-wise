# ... (existing imports and app_name)
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # ... (existing paths)
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'), # <-- Add this line
]