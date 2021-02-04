from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('insert/', views.data_insert),
    path('<int:itemid>/', views.item_detail),
    path('rating/', views.rating_list),
    path('rating/<int:r_id>/', views.rating_detail),
    path('rec_test/', views.rec_cf_test),
]
