from django.views.generic import ListView
from .models import Prop


class PropList(ListView):
    model = Prop
    context_object_name = 'props'

