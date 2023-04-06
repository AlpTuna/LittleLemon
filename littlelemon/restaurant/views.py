from django.shortcuts import render
from django.http import HttpResponse
import rest_framework
from rest_framework.generics import RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class MenuItemView(rest_framework.views.APIView):
    def get(self,request):
        items = Menu.objects.all()
        items = MenuSerializer(items,many=True)
        return Response(items.data)
    
    def post(self,request):
        newItem = Menu.objects.create(title = request.POST["name"],price=request.POST["price"],inventory = request.POST["inventory"])
        newItem.save()
        newItem = MenuSerializer(newItem)
        return Response(newItem.data,status = 200)
        
class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    def get(self,request,pk):
        item = Menu.objects.filter(id=pk)
        if item:
            item = MenuSerializer(item)
            return Response(item.data)
        else:
            return Response(f"No item with pk: {pk}")
        

class BookingView(RetrieveUpdateAPIView,DestroyAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        booking = Booking.objects.filter(id=pk)
        if booking:
            booking = booking[0]
            booking = BookingSerializer(booking)
            return Response(booking.data)
        else:
            return Response(f"No item with pk: {pk}")
        
class BookingPostView(RetrieveUpdateAPIView,DestroyAPIView):
    def post(self,request):
        newBooking = Booking.objects.create(name = request.POST["name"],no_of_guests=request.POST["guests"],
                                         booking_time = request.POST["booking_time"])
        newBooking.save()
        newBooking = BookingSerializer(newBooking)
        return Response(newBooking.data,status = 200)
    

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"}) 