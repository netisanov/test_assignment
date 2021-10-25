from django.urls import path
from . import views


# API endpoints
urlpatterns = [
    path('', views.api_root),
    path('persons/',
        views.PersonList.as_view(),
        name='person-list'),
    path('persons/<int:pk>/',
        views.PersonDetail.as_view(),
        name='person-detail'),
    path('coordinates/',
        views.CoordinateList.as_view(),
        name='coordinate-list'),
    path('coordinates/<int:pk>/',
        views.CoordinateDetail.as_view(),
        name='coordinate-detail'),
    path('generator/', views.coordinates_generator),
]