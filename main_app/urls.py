from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('poems/', views.poems_index, name='index'),
    path('poems/<int:poem_id>/', views.poem_details, name='detail'),
    path('poems/create/', views.poemCreate.as_view(), name='poem_create'),
    path('poems/<int:pk>/update/', views.poemUpdate.as_view(), name='poem_update'),
    path('poems/<int:pk>/delete', views.poemDelete.as_view(), name='poem_delete'),
    path('poems/<int:poem_id>/add_read', views.add_read, name='add_read'),
    path('author/', views.AuthorList.as_view(), name="author_index"),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name="author_detail"),
    path('author/create/', views.AuthorCreate.as_view(), name="author_create"),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name="author_update"),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name="author_delete"),
    path('poems/<int:poem_id>/assoc_author/<int:author_id>/', views.assoc_author, name='assoc_author'),
    path('poems/<int:poem_id>/unassoc_author/<int:author_id>/', views.unassoc_author, name='unassoc_author')
]