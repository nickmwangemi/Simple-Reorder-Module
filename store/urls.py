from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.ProductView.as_view(), name='Product'),
    path('store/<int:pk>/', views.ProductDetailView.as_view(), name='Product Detail')

]