from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [ 
    path('reorders/', views.ReorderView.as_view(), name='Reorder'),
    path('reorders/<int:pk>/', views.ReorderDetailView.as_view(), name='Reorder Detail'),
    path('process_reorder/<int:pk>/', views.process_reorder, name='Process Reorder'),
]