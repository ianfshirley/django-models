from django.urls import path

from .views import HomePageView, SnackDetailsView, SnackListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('snack/', SnackListView.as_view(), name='snack_list'),
    path('snack/<int:pk>/', SnackDetailsView.as_view(), name='snack_details'),
]