from django.urls import path 
from .views import MenuItemView,SingleMenuItemView,BookingView,BookingPostView
  
urlpatterns = [ 
    path('items/', MenuItemView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/tables/<int:pk>', BookingView.as_view()),
    path('booking/tables/', BookingPostView.as_view()),
]