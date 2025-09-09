from django.contrib import admin
from .models import TiposExames, PedidosExames, SolicitacaoExame
from .models import AcessoMedico

admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)
admin.site.register(AcessoMedico)