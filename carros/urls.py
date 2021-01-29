from django.urls import path
from . views import lista_carros, novos_carros, alterar_carros, deletar_carros


urlpatterns = [
    path('', lista_carros, name='lista_carros'),
    path('novos/', novos_carros, name='novos_carros'),
    path('alterar/<int:id>', alterar_carros, name='alterar_carros'),
    path('deletar/<int:id>', deletar_carros, name='deletar_carros'),
]