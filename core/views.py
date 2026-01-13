from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario, Curso, Material, Turma, Chamada
from .serializers import (
    UsuarioSerializer, CursoSerializer, MaterialSerializer, 
    TurmaSerializer, ChamadaSerializer
)

class MeViewSet(viewsets.ReadOnlyModelViewSet):
    """Retorna os dados do próprio usuário logado"""
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Usuario.objects.filter(id=self.request.user.id)
    
    @action(detail=False, methods=['get'])
    def perfil(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'ALUNO' and user.curso:
            return Material.objects.filter(curso=user.curso)
        return Material.objects.all()

class TurmaViewSet(viewsets.ModelViewSet):
    serializer_class = TurmaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'PROFESSOR':
            return Turma.objects.filter(professor=user)
        elif user.tipo == 'ALUNO':
            return user.turmas_matriculadas.all()
        return Turma.objects.all()

    def perform_create(self, serializer):
        serializer.save(professor=self.request.user)

class ChamadaViewSet(viewsets.ModelViewSet):
    serializer_class = ChamadaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.tipo == 'PROFESSOR':
            return Chamada.objects.filter(turma__professor=user)
        return Chamada.objects.none()