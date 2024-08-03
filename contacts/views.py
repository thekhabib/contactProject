from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import ContactForm
from .models import Contact


# Create your views here.
def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_list')

    form = ContactForm()
    context = {
        'form': form,
    }

    return render(request, 'contact_form.html', context)


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy("contacts_list")


def contacts_list(request):
    contacts = Contact.objects.filter(active=True).order_by('id')
    context = {
        'contacts': contacts,
    }

    return render(request, 'contacts_list.html', context)


class ContactListView(ListView):
    model = Contact
    template_name = 'contacts_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.filter(active=True).order_by('id')
