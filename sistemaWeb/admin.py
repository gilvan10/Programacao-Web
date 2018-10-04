from django.contrib import admin
from .models import Clientes
from .models import Empresas
from .models import LancamentosReceber

admin.site.register(Clientes)
admin.site.register(Empresas)
admin.site.register(LancamentosReceber)

