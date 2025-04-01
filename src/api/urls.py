from os.path import basename

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"todolists", views.TodoListViewSet)
router.register(r"todos", views.TodoViewSet)

router.register(r"ready", views.ReadyViewSet, basename="ready")
router.register(r"health", views.LivenessViewSet, basename="health")

app_name = "api"
urlpatterns = [
    path("", include(router.urls))
]
