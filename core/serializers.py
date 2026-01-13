from rest_framework import serializers
from .models import Usuario, Curso, Material, Turma, Chamada

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'tipo', 'curso']

class MaterialSerializer(serializers.ModelSerializer):
    nome_curso = serializers.CharField(source='curso.nome', read_only=True)

    class Meta:
        model = Material
        fields = ['id', 'titulo', 'link', 'curso', 'nome_curso']

class TurmaSerializer(serializers.ModelSerializer):
    professor_nome = serializers.CharField(source='professor.get_full_name', read_only=True)
    # Mostra os dados dos alunos na leitura, mas aceita apenas IDs na escrita
    alunos_detalhes = UsuarioSerializer(source='alunos', many=True, read_only=True)
    alunos = serializers.PrimaryKeyRelatedField(many=True, queryset=Usuario.objects.filter(tipo='ALUNO'))

    class Meta:
        model = Turma
        fields = ['id', 'nome', 'dia_semana', 'horario', 'professor', 'professor_nome', 'alunos', 'alunos_detalhes']
        extra_kwargs = {'professor': {'read_only': True}} # Professor é pego do usuário logado

class ChamadaSerializer(serializers.ModelSerializer):
    turma_nome = serializers.CharField(source='turma.nome', read_only=True)
    
    class Meta:
        model = Chamada
        fields = ['id', 'turma', 'turma_nome', 'data', 'alunos_presentes']