from django.urls import path

from webapp.views import good_list_view, good_create_view, good_view, delete_good

urlpatterns = [
    path('', good_list_view, name="index"),
    path('good/add/', good_create_view, name="good_add"),
    path('good/<int:pk>', good_view, name="good_view"),
    path('delete/<int:good_id>/', delete_good),
]
