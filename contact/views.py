from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = Contact(name=name, email=email, subject=subject, message=message)
        contact_data.save()
        return render(request, 'contact.html')
    return render(request, 'contact.html')
