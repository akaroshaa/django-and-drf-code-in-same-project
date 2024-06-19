from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", views.ProductModelViewSet, basename="prods")
router.register("employees", views.EmployeeModelViewSet, basename="emps")

urlpatterns = [
    path('', include(router.urls)),
]
