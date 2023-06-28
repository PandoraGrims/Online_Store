from django.urls import path

from webapp.views import good_list_view, good_create_view, good_view, delete_good, category_add_view, category_view

urlpatterns = [
    path('', good_list_view, name="index"),
    path('goods/', good_list_view, name="index"),
    path('good/add/', good_create_view, name="good_add"),
    path('good/<int:pk>', good_view, name="good_view"),
    path('delete/<int:good_id>/', delete_good, name="delete_good"),
    path('categories/add/', category_add_view, name='category_add'),
    path('categories/', category_view, name='category_view'),
]
