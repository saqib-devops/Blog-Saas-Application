from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'public_website/home.html'
