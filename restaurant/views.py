from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Booking, Menu
from . serializers import BookingSerializer, MenuSerializer, UserSerializer
# Create your views here.
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

class bookingview(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many= True)
        return Response(serializer.data)
    


class menuview(APIView):
    def post(self, request):
        serializer = MenuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data})
        


def index(request):
    return render(request, 'index.html')

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer()


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer()


class BookingViewSet (ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 