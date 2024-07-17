from django.urls import path
from .views import UserRegisterView

# URL patterns for the user_auth app
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # This URL pattern maps the 'register/' URL to the UserRegisterView
    # It uses Django's class-based view system to handle user registration
    # The 'name' parameter allows for easy reference to this URL in templates and views
]
