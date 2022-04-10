from django.urls import include, path

from reservation.views import (
    ChambreRetrieveUpdateView,
    ChambreListCreateAPIView,
    ServiceRetrieveUpdateView,
    ServiceListCreateAPIView,
    UniversiteRetrieveUpdateView,
    UniversiteListCreateAPIView,
)

urlpatterns = [
    path(
        "chambres/",
        ChambreListCreateAPIView.as_view(),
        name="chambres",
    ),
    path(
        "chambres/<int:pk>/",
        ChambreRetrieveUpdateView.as_view(),
        name="chambre_info",
    ),
    path(
        "services/",
        ServiceListCreateAPIView.as_view(),
        name="services",
    ),
    path(
        "services/<int:pk>/",
        ServiceRetrieveUpdateView.as_view(),
        name="service_info",
    ),
    path(
        "universites/",
        UniversiteListCreateAPIView.as_view(),
        name="universites",
    ),
    path(
        "universites/<int:pk>/",
        UniversiteRetrieveUpdateView.as_view(),
        name="universite_info",
    ),
]
