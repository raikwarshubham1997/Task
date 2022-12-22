from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import countryDetails
from .serializers import CountryDetaliSerializer
from rest_framework import status
from rest_framework.views import APIView


import requests
import string
from bs4 import BeautifulSoup
import pandas as pd
import pywhatkit as pwt
 


class CountryAPI(APIView):
    def get(self, request, pk=None, format=None, country=None):
        id = pk
        if id is not None:
            prod = countryDetails.objects.get(id=id)
            serializer = CountryDetaliSerializer(prod)
            return Response(serializer.data)
        
        
        url = "https://en.wikipedia.org/wiki/India"
        table_class = "infobox ib-country vcard"
        
        
        # STEP1: get the html
        r = requests.get(url)
        # htmlContent = r.content
        # print(htmlContent)
        soup = BeautifulSoup(r.text, 'html.parser')
        detail_table = soup.find('table', attrs={'class': table_class})
        # print("THIS",detail_table)
        df = pd.read_html(str(detail_table))
        print(df)
        
        
        # print(soup.find('table')['id'])
        
        prod = countryDetails.objects.all()
        serializer = CountryDetaliSerializer(prod, many=True)
        return Response(serializer.data)
        

        # Entry_input = input("Search: ")
        # u_i =  string.capwords(Entry_input)
































#     def post(self, request, format=None):
#         serializer = CountryDetaliSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, pk, format=None):
#         id = pk
#         prod = countryDetails.objects.get(pk=id)
#         serializer = CountryDetaliSerializer(prod, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def patch(self, request, pk, format=None):
#         id = pk
#         prod = countryDetails.objects.get(pk=id)
#         serializer = CountryDetaliSerializer(prod, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)

#     def delete(self, request, pk, format=None):
#         id = pk
#         prod = countryDetails.objects.get(pk=id)
#         prod.delete()
#         return Response({'msg': 'Data Deleted'})


# #Function based api

# # @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# # def product_api(request, pk=None):
# #     if request.method == 'GET':
# #         id = pk
# #         if id is not None:                      
# #             prod = Product.objects.get(id=id)
# #             serializer = CountryDetaliSerializer(prod)
# #             return Response(serializer.data)

# #         prod = Product.objects.all()
# #         serializer = ProductSerializer(prod, many=True)
# #         return Response(serializer.data)

        



