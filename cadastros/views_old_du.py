from django.views.generic.edit import CreateView #createView usado para formularios
from .models import Campo, Atividade, Campus #importei minhas classes modelo
from django.urls import reverse_lazy

# Create your views here.

class CampoCreate(CreateView):
    model = Campo #model recebe o modelo que iremos gravar
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index') #define aqui para onde vai redirecionar em caso de OK

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')