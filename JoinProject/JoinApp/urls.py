from django.urls import path
from . import views  # If using the StateListView

urlpatterns = [
    path('join/', views.StateListView.as_view(), name='get_states'),  # Optional endpoint
]