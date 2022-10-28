from django.urls import path

from .views import GelleryView, GelleryCreateView, GelleryUpdateView, GelleryDeleteView


urlpatterns = [
    path('api/v1/gellery/', GelleryView.as_view(), name='gellery'),
    path('api/v1/gellery/create/', GelleryCreateView.as_view(), name='craete_gelery'),
    path('api/v1/gellery/<int:pk>', GelleryUpdateView.as_view()),
]

