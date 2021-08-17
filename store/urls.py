from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [ 
    path('', views.ProductView.as_view(), name='Product'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='Product Detail'),
    path('sell/<int:pk>/', views.sell_product, name='Sell'),
    path('make_reorder/<int:pk>/', views.reorder_product, name='Reorder Product'),
]