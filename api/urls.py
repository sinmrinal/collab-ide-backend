from django.urls import include, path

from . import views

urlpatterns = [
    path('boilerPlate/<str:language>/', views.boiler_plate),
    path('compile/', views.compile_code),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('createRoom/', views.create_room),
    path('joinRoom/', views.join_room),
    path('check/', views.check)
]
