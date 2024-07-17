from django.contrib import admin
from .models import Myband

# Register your models here.

admin.site.register(Myband)
"""
Registers the Myband model with the Django admin site.

By registering the Myband model, it becomes accessible and manageable
through the Django admin interface. This allows administrators to 
add, edit, and delete instances of the Myband model from the admin panel.

Attributes:
    Myband (model): The model to be registered with the admin site.
"""
