from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Mp3


class Mp3List(generic.ListView):
	model = Mp3
	queryset = Mp3.objects.published()
	paginate_by = 10
	template_name = "nump3/mp3_list.html"


class Mp3Detail(generic.DetailView):
	model = Mp3
	template_name = "nump3/mp3_detail.html"