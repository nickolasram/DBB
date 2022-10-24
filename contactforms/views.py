from django.template.response import SimpleTemplateResponse
from django.views.generic.edit import FormView
from .forms import *

class ContactFormView(FormView):
    template_name = 'contactforms/contact.html'
    form_class = Contact_Form

    def form_valid(self, form):
        form.send_email()
        return SimpleTemplateResponse('contactforms/sent-success.html')


class Bug_Form_View(FormView):
    template_name = 'contactforms/bug.html'
    form_class = Bug_Form

    def form_valid(self, form):
        form.send_email()
        return SimpleTemplateResponse('contactforms/sent-success.html')