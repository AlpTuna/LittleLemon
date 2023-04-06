from django.urls import path 
from .views import MenuItemView,SingleMenuItemView,BookingView,BookingPostView,msg
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('items/', MenuItemView.as_view()),
    path('items/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/tables/<int:pk>', BookingView.as_view()),
    path('booking/tables/', BookingPostView.as_view()),
    path('api-token-auth/',obtain_auth_token),
    path("message",msg),
]