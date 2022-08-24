from django.urls import path
from .views import myview, new, update, test, ProductDetailView, ProductDetailActions, ManufacturerDetailView, ManufacturerDetailActions

urlpatterns = [
    path('detail/', ProductDetailView.as_view()),
    path('<int:ids>/', ProductDetailActions.as_view()),
    path('manufacturer/', ManufacturerDetailView.as_view()),
    path('manufacturer/<int:ids>/', ManufacturerDetailActions.as_view()),
    path("new/", new),
    path('test/', test)
]
