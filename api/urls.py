from django.urls import path
from . import views


#from .views import MyModelListCreate


urlpatterns = [

    path('', views.apiOverview, name="api-overview"),
    path('mymodel-list/', views.mymodelList, name="mymodel-list"),
    path('mymodel-detail/<str:pk>/', views.mymodelDetail, name="mymodel-detail"),
    path('mymodel-create/', views.mymodelCreate, name="mymodel-create"),
    path('mymodel-update/<str:pk>/', views.mymodelUpdate, name="mymodel-update"),
	path('mymodel-delete/<str:pk>/', views.mymodelDelete, name="mymodel-delete"),

    #path('' , views.index , name= 'index') ,
    #path('about' , views.about , name= 'about') ,
    
    #path('api/data/', MyModelListCreate.as_view(), name='my_model-list-create'),

]
