from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.http import Http404
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import filters
from rest_framework import generics
#from rest_framework import viewsets

# Create your views here.

class ProduitList(APIView):

	def get(self,request,format=None):
		produits = Produit.objects.all()[:4]
		serializer = ProduitSerializer(produits, many = True)
		return Response(serializer.data)


class ProduitDetail(APIView):
	def get_object(self, product_slug):
		try:
			return Produit.objects.get(slug=product_slug)
		except Produit.DoesNotExist:
			raise Http404
	def get(self, request,  product_slug, format=None):
		produit= self.get_object( product_slug)
		Serializer = ProduitSerializer(produit)
		return Response(Serializer.data)


class CategorieDetail(APIView):
	def get(self,request,idCat,format=None):
		produits = Produit.objects.filter(category = idCat)
		serializer = ProduitSerializer(produits, many = True)
		return Response(serializer.data)

@api_view(['POST'])
def search(request):
	query=request.data.get('query','')
	if query:
		products = Produit.objects.filter(Q(nom=query) | Q(description_icontains=query))
		serializer = ProduitSerializer(products, many = True)
		return Response(serializer.data)
	else:
		return Response({'products':[]})



class UserListView(generics.ListAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'description']
