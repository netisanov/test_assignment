from django.urls import path

from .CoordinateViews import CoordinateViews
from .PersonViews import PersonViews
from .GeneratorViews import GeneratorViews
from . import views


urlpatterns = [
    path('', views.ApiRoot.as_view()),
    path('persons/',
         PersonViews.PersonList.as_view(),
         name='person-list'),
    path('persons/<int:pk>/',
         PersonViews.PersonDetail.as_view(),
         name='person-detail'),
    path('coordinates/',
         CoordinateViews.CoordinateList.as_view(),
         name='coordinate-list'),
    path('coordinates/<int:pk>/',
         CoordinateViews.CoordinateDetail.as_view(),
         name='coordinate-detail'),
    path('generator/', GeneratorViews.GeneratorView.as_view()),
]
