from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime
from .models import Hotel, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    res_for = serializers.StringRelatedField(read_only = True)
    
    class Meta:
        model = Reservation
        
        fields = "__all__"
            
    def validate(self, instance):
        d3 = str(instance["signing_out_on"])
        d4 = str(instance["signing_in_on"])
        d1 = datetime.strptime(d4, "%Y-%m-%d")
        d2 = datetime.strptime(d3, "%Y-%m-%d")
        
        if (d2 - d1).days != instance["duration_of_stay"]:
            raise serializers.ValidationError("Duration does not match the dates passed")
        
        else:
            return instance
        


class HotelSerializer(serializers.ModelSerializer):
    hotel = ReservationSerializer(many = True, read_only = True)
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Hotel
        fields = "__all__"
        
        
    def get_len_name(self, object):
        length = len(object.name)
        return length

class UserSerializer(serializers.ModelSerializer):   
    res_for = ReservationSerializer(many = True, read_only = True) 
    class Meta:
        model = User
        fields = "__all__"
