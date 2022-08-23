from cgitb import Hook
from django.urls import path
from .views import HotelDetailActions, HotelDetailView, ReservationDetailView, UserDetailView, ReservationDetailActions

urlpatterns = [
    path("", ReservationDetailView.as_view()),
    path("hotel/", HotelDetailView.as_view()),
    path("<int:ids>/", HotelDetailActions.as_view()),
    path("res/<int:ids>/", ReservationDetailActions.as_view()),
    path("users/", UserDetailView.as_view()),
]
