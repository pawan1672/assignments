from django.shortcuts import render

# Create your views here.
import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
# for filtering purpose
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


def index(request):
    return render(request,'index.html')

def product_list(request):
    products = Product.objects.active()
    return render(request, 'product_list.html', {'products': products})

@api_view(['POST'])
def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('file'):
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        created_count = 0
        errors = []

        for row in reader:
            serializer = ProductSerializer(data=row)
            if serializer.is_valid():
                serializer.save()
                created_count += 1
            else:
                errors.append(serializer.errors)

        if errors:
            return Response({'message': 'Some rows failed to process', 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': f'{created_count} products created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
   
class ProductListView(generics.ListAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     filter_backends = [DjangoFilterBackend]
     filterset_class = ProductFilter
    
    
class ProductSingleView(generics.RetrieveAPIView):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_destroy(self, instance):
        instance.delete() 