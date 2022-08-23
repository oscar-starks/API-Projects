from django.shortcuts import render
from rest_framework.views import APIView
from funct_api.models import Reservation, Hotel
from .serializers import HotelSerializer, ReservationSerializer, User, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

    


class UserDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        ip = x_forwarded_for
        print(ip)
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)
        
    def post(self, request):
    
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class ReservationDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reservation = Reservation.objects.all()
        serializer = ReservationSerializer(reservation, many = True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ReservationSerializer(data = request.data)
        data = request.data
        user = request.user
        # print(data["hotel"], "---------------------------------------------")
        print(data)
        hotel_id = data["hotel"]
        hotel = Hotel.objects.get(id = hotel_id)
        
        if serializer.is_valid():
            serializer.save(res_for = user)
            hotel.number_of_reservations = hotel.number_of_reservations + 1
            hotel.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ReservationDetailActions(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        try:
            data = Reservation.objects.get(id = ids)
            serializer = ReservationSerializer(data, many = False)
            return Response(serializer.data)

        except:
            print( "-----------------------------")
            data = Reservation.objects.get(id = 2)
            serializer = ReservationSerializer(data, many = False)
            return Response(serializer.data)

    def put(self, request, ids):
        res = request.user
        reservation = Reservation.objects.get(id = ids)
        serializer = ReservationSerializer(instance = reservation, data = request.data)
        
        if serializer.is_valid():
            serializer.save(res_for = res)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self, request, ids):
        reservation = Reservation.objects.get(id = ids)
        reservation.delete()
        return Response({"content":"deleted"}) 
    
    
class HotelDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        hotel = Hotel.objects.all()
        serializer = HotelSerializer(hotel, many = True)
        return Response(serializer.data)
        
    def post(self, request):
    
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class HotelDetailActions(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, ids):
        print(request.query_params, "---------------------------------")
        try:
            data = Hotel.objects.get(id = ids)
            serializer = HotelSerializer(data, many = False)
            return Response(serializer.data)

        except:
            print( "-----------------------------")
            data = Hotel.objects.get(id = 2)
            serializer = HotelSerializer(data, many = False)
            return Response(serializer.data)

    def put(self, request, ids):
        hotel = Hotel.objects.get(id = ids)
        serializer = HotelSerializer(instance = hotel, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self, request, ids):
        hotel = Hotel.objects.get(id = ids)
        hotel.delete()
        return Response({"content":"deleted"}) 