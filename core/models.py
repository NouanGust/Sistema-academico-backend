from django.db import models
from django.contrib.auth.models import AbstractUser


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Usuario(AbstractUser):
    TIPOS = (
        ('ADMIN', 'Admin'),
        ('PROFESSOR', 'Professor'),
        ('ALUNO', 'Aluno'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS, default='ALUNO')
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    
class Material(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.URLField(help_text="Link para o arquivo")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='materias')
    
    def __str__(self):
        return self.titulo


class Turma(models.Model):
    nome = models.CharField(max_length=100)
    dia_semana = models.CharField(max_length=20)
    horario = models.TimeField()
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo': 'PROFESSOR'}, related_name='turmas_ministradas')
    alunos = models.ManyToManyField(Usuario, limit_choices_to={'tipo': 'ALUNO'}, related_name='turmas_matriculadas', blank=True)
    
    def __str__(self):
        return f"{self.nome} - {self.professor.username}"

class Chamada(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='chamadas')
    data = models.DateField(auto_now_add=True)
    alunos_presentes = models.ManyToManyField(Usuario, limit_choices_to={'tipo': 'ALUNO'}, related_name='presencas')
    
    def __str__(self):
        return f"Chamada {self.turma} - {self.data}"