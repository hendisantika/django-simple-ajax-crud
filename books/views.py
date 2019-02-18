# Create your views here.
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import BookForm


def book_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = BookForm()

    context = {'form': form}
    data['html_form'] = render_to_string('books/includes/partial_book_create.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)
