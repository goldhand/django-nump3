from django.views import generic

from nupages.models import Page

from .models import Mp3


class Mp3List(generic.ListView):
	model = Mp3
	queryset = Mp3.objects.published()
	paginate_by = 10
	template_name = "nump3/mp3_list.html"


class Mp3Detail(generic.DetailView):
	model = Mp3
	template_name = "nump3/mp3_detail.html"

	def get_context_data(self, **kwargs):
		context = super(Mp3Detail, self).get_context_data(**kwargs)
		page = Page.objects.get_or_404(slug=context['page_slug'])
		context.update({'page': page})
		if page.custom_template:
			self.template_name = "nupages/%s.html" % page.slug
		return context