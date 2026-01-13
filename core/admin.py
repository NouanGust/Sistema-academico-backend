from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Curso, Material, Turma, Chamada

# Configuração especial para o Usuário Customizado (para aparecer os campos Tipo e Curso)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Acadêmicas', {'fields': ('tipo', 'curso')}),
    )
    list_filter = ('tipo', 'curso') # Filtros laterais
    list_display = ('username', 'email', 'first_name', 'tipo', 'curso') # Colunas da tabela

# Registrando tudo no painel
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Curso)
admin.site.register(Material)
admin.site.register(Turma)
admin.site.register(Chamada)