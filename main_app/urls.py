from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    # route for cats index
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path(
        'cats/<int:cat_id>/add-feeding/', 
        views.add_feeding, 
        name='add-feeding'
    ),
    # new routw used ti create a cat
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    # # Add the new routes below
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),

]
