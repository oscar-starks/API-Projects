# from django.shortcuts import render

from django.http import JsonResponse
# import json
from product.models import Product, Manufacturer
# from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ProductSerializers, ManufacturerSerializers, ProductSerializer

#########################################################################################################################################################

class ProductDetailView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many = True)
        return Response(serializer.data)
        
    def post(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

#########################################################################################################################################################       
        
class ProductDetailActions(APIView):
    def get(self, request, ids):
        datas = Product.objects.get(id = ids)
        serializer = ProductSerializers(datas, many = False)
        return Response(serializer.data)
       
    def put(self, request, ids):
        products = Product.objects.get(id = ids)
        serializer = ProductSerializers(instance = products, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self, request, ids):
        products = Product.objects.get(id = ids)
        products.delete()
        return Response({"content":"deleted"})
    
#########################################################################################################################################################


class ManufacturerDetailView(APIView):
    def get(self, request):
        manufacturer = Manufacturer.objects.all()
        serializer = ManufacturerSerializers(manufacturer, many = True)
        return Response(serializer.data)
        
    def post(self, request):
        manufacturer = Manufacturer.objects.all()
        serializer = ManufacturerSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
 
#########################################################################################################################################################      
 
        
class ManufacturerDetailActions(APIView):
    def get(self, request, ids):
        manufacturer = Manufacturer.objects.get(id = ids)
        serializer = ProductSerializers(manufacturer, many = False)
        return Response(serializer.data)
        
    def put(self, request, ids):
        manufacturer = Manufacturer.objects.get(id = ids)
        serializer = ManufacturerSerializers(instance = manufacturer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self, request, ids):
        manufacturer = Manufacturer.objects.get(id = ids)
        manufacturer.delete()
        return Response({"content":"deleted"})

#########################################################################################################################################################



@api_view(['GET', 'POST'])
def test(request):
    if request.method == "GET":
        model_data = Product.objects.all()
        serializer = ProductSerializer(model_data, many = True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(["GET"])
def myview(request, id):
    try:
        model_data = Product.objects.get(id = id)
        serializer = ProductSerializer(model_data, many = False)
        
        return Response(serializer.data) 
    except:
        model_data = Product.objects.get(id = 1)
        serializer = ProductSerializer(model_data, many = False)
        
        return Response(serializer.data) 
    
@api_view(["POST"])
def new(request):
    
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(["POST"])
def update(request, id):
    task = Product.objects.get(id = id)
    serializer = ProductSerializer(instance = task, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 
    
    
    
    # model_data = Product.objects.all().order_by("?").first()
    # mylist = {
    #     "hey":"helllo"
    # }
    
    # if model_data:
    #     data = model_to_dict(model_data, fields=["name", "content", "price"])
    
        
    # if request.method == "POST":
    #     return Response({"detail":"POST not allowed"}, status = 405)
    # if model_data:
    #     data['id'] = model_data.id
    #     data['name'] = model_data.name 
    #     data['price'] = model_data.price
    #     data['content'] = model_data.content
        
    #     print(request.GET)
    # return JsonResponse(data)


# def myview(request):
#     data = {}
#     body = request.body
#     print(request.GET)
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
    
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     # print(request.headers)
#     return JsonResponse(data)
