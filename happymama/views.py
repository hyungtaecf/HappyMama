from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.template.loader import get_template
from django.views.generic import TemplateView, FormView

from .forms import ContactForm

class Home(FormView):
    form_class = ContactForm
    template_name = 'index.html'
    success_url = '/form-success/'

    def form_invalid(self, form):
        response = super(Home, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        template = get_template('contact_message.txt')
        content = {
            'name': self.request.POST.get('name'),
            'fonetic': self.request.POST.get('fonetic'),
            'email': self.request.POST.get('email'),
            'phone': self.request.POST.get('phone'),
            'message': self.request.POST.get('message'),
        }
        content = template.render(content)
        email = self.request.POST.get('email')
        email = EmailMessage(
            "New contact form email",
            content,
            "HappyMama",
            ['htfigur@gmail.com'], # 'info@happymama.jp'
            headers = { 'Reply To': email}
        )
        email.send()
        data = {
            'success': True,
        }
        return JsonResponse(data)

class TaxAuditing(TemplateView):
    template_name = 'tax-auditing.html'
