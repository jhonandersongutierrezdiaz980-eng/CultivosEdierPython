from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cultivo
from .forms import CultivoForm

# Listar todos los cultivos (R - Read)
class CultivoListView(ListView):
    model = Cultivo
    template_name = 'cultivos/cultivo_list.html'
    context_object_name = 'cultivos'

# Crear un nuevo cultivo (C - Create)
class CultivoCreateView(CreateView):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'cultivos/cultivo_form.html'
    success_url = reverse_lazy('cultivo_list')

# Editar un cultivo existente (U - Update)
class CultivoUpdateView(UpdateView):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'cultivos/cultivo_form.html'
    success_url = reverse_lazy('cultivo_list')

# Eliminar un cultivo (D - Delete)
class CultivoDeleteView(DeleteView):
    model = Cultivo
    template_name = 'cultivos/cultivo_confirm_delete.html'
    success_url = reverse_lazy('cultivo_list')
