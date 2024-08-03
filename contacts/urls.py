from django.urls import path
from .views import contact_form_view, ContactCreateView, contacts_list, ContactListView

urlpatterns = [
    # path('', contact_form_view, name='contact_form'),
    path('', ContactCreateView.as_view(), name='contact_form'),
    # path('xabarlar/', contacts_list, name='contacts_list'),
    path('xabarlar/', ContactListView.as_view(), name='contacts_list'),
]
