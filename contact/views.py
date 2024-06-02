from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            description = form.cleaned_data['description']
            attachment = form.cleaned_data['attachment']
            terms_accepted = form.cleaned_data['terms_accepted']
            
            # Create the Contact object
            contact = Contact(
                name=name,
                email=email,
                phone_number=phone_number,
                description=description,
                attachment=attachment,
                terms_accepted=terms_accepted
            )
            contact.save()

            # Redirect to a success page
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})



def contact_success_view(request):
    return render(request, 'contact/contact_success.html')