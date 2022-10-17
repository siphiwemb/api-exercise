from django.urls import path
from .views import TitanicView 

urlpatterns = [
    path("people", TitanicView.as_view()),
    path("people/<str:uuid>", TitanicView.as_view())
]