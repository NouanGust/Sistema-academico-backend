from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MeViewSet, MaterialViewSet, TurmaViewSet, ChamadaViewSet

router = DefaultRouter()
router.register(r'me', MeViewSet, basename='me')
router.register(r'materiais', MaterialViewSet, basename='material')
router.register(r'turmas', TurmaViewSet, basename='turma')
router.register(r'chamadas', ChamadaViewSet, basename='chamada')

urlpatterns = [
    path('', include(router.urls)),
]