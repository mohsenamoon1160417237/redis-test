from django.urls import path
from .views import intialize_views, add_views, expire_views, expire_at

urlpatterns = [

    path('init/', intialize_views, name='init_views'),
    path('add/', add_views, name='add_views'),
    path('expire/', expire_views, name='expire_views'),
    path('expire/at/', expire_at, name='expire_at'),
]