# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render_to_response
from cibereducacao.books.models import Book

def search(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error.append('Enter a search term.')
        elif len(q) > 20:
            error.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_results.html',
                {'books':books,'query': q})
    
    return render_to_response('search_form.html',{'error':error})
