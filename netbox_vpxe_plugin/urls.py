from django.urls import path
from . import views


urlpatterns = (
    # Boot Profiles
    path('profiles/', views.BootProfileListView.as_view(), name='boot_profile_list'),
    path('profiles/add/', views.BootProfileListView.as_view(), name='boot_profile_add'),
    path('profiles/delete/', views.BootProfileListView.as_view(), name='boot_profile_bulk_delete'),
    path('profile/<int:pk>/', views.BootProfileListView.as_view(), name='boot_profile'),
    path('profile/<int:pk>/edit/', views.BootProfileListView.as_view(), name='boot_profile_edit'),
    path('profile/<int:pk>/delete/', views.BootProfileListView.as_view(), name='boot_profile_delete'),
)
