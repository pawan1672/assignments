from django.contrib import admin
from django.urls import path,include
from . import views
from .views import upload_csv,ProductCreateView,ProductDeleteView,ProductListView,ProductSingleView,ProductUpdateView,product_list
from .views import ProductRetrieveUpdateDestroy
from rest_framework.routers import DefaultRouter


urlpatterns = [
    
    path('product/',product_list,name='product-list'),
    path('productinapi',ProductListView.as_view(), name='product-list'),
    path('',views.index,name='index'),
    path('product/create/',ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/',ProductSingleView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/',ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/upload_csv/', upload_csv, name='upload-csv'),
    
    
    
    ]

