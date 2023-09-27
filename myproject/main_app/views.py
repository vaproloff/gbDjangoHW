from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class AboutView(TemplateView):
    template_name = 'main_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О себе'
        return context
