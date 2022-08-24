
from rest_framework import serializers
from product.models import Product, Manufacturer

#########################################################################################################################################################
class ProductSerializers(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = "__all__"
        
        
    def get_len_name(self, object):
        length = len(object.name)
        return length

#########################################################################################################################################################        
        
class ManufacturerSerializers(serializers.ModelSerializer):
    manufacturer = ProductSerializers(many = True, read_only = True)
    
    class Meta:
        model = Manufacturer
        
        fields = "__all__"
        
        # def get_lens(self, object):
        #     length = len(object.name)
        #     return length
      
#########################################################################################################################################################  
        
def val(value):
    if len(value) < 2:
        raise serializers.ValidationError("name too short")        
    else:
        return value
        
        
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(validators = [val] )
    content = serializers.CharField()
    price = serializers.IntegerField()
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
    
    def validate(self, instance):
        if instance["name"] == instance["content"]:
            raise serializers.ValidationError("Name is equal to the content")
        else:
            return instance
        
    def validate_price(self, value):
        if value > 5:
            raise serializers.ValidationError("amount too large")
        else:
            return value
#########################################################################################################################################################       
        
        
    