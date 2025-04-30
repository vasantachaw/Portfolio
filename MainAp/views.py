from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from MainAp.models import Contact # import your model

def home(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not message:
            messages.error(request, "Please fill in all required fields.")
            return redirect('contact')

        # Save to the database
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        # Send email (optional)
        full_message = f"From: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
        try:
            send_mail(
                subject,
                full_message,
                email,
                ['vasantachaw@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('home')

    return redirect('contact')
