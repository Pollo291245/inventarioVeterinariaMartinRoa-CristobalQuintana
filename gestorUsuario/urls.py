from django.urls import path
from gestorUsuario.views import signUpView

urlpatterns = [
    path('registro/', signUpView.as_view(),name='registro'),
]