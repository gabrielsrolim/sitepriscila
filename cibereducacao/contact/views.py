# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render_to_response
from cibereducacao.contact.forms import ContactForm

def contact(request):
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_email(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject':'I love your site!'})
    return render_to_response('contact_form.html',{'form': form})
