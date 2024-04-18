from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyModelSerializer
from .models import MyModel

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/mymodel-list/',
		'Detail View':'/mymodel-detail/<str:pk>/',
		'Create':'/mymodel-create/',
		'Update':'/mymodel-update/<str:pk>/',
		'Delete':'/mymodel-delete/<str:pk>/',
		}

	return Response(api_urls)
# create views for displaying users

@api_view(['GET'])
def mymodelList(request):
	mymodels = MyModel.objects.all().order_by('-id')
	serializer = MyModelSerializer(mymodels, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def mymodelDetail(request, pk):
	mymodels = MyModel.objects.get(id=pk)
	serializer = MyModelSerializer(mymodels, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def mymodelCreate(request):
	serializer = MyModelSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def mymodelUpdate(request, pk):
	mymodel = MyModel.objects.get(id=pk)
	serializer = MyModelSerializer(instance=mymodel, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def mymodelDelete(request, pk):
	mymodel = MyModel.objects.get(id=pk)
	mymodel.delete()

	return Response('Item succsesfully delete!')

