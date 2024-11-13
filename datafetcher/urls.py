from django.urls import path 
from .views import FetchCreateView, FetchUpdateView

urlpatterns = [
    path('', FetchCreateView.as_view(), name='home'),
    path('fetch/<int:pk>/', FetchUpdateView.as_view(), name='update'),
    
]