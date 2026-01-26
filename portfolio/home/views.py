from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    # Handle contact form submission
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message_text = form.cleaned_data["message"]

            subject = f"Portfolio Contact from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}"
            recipient = getattr(settings, "DEFAULT_TO_EMAIL", settings.EMAIL_HOST_USER)
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                success_msg = "Message sent successfully. Thank you — I'll get back to you soon."
                # If AJAX request, return JSON
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({"status": "success", "message": success_msg})

                messages.success(request, success_msg)
            except Exception as e:
                err_msg = f"Error sending message: {e}"
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({"status": "error", "message": err_msg}, status=500)
                messages.error(request, err_msg)

            # Redirect back to the contact section for non-AJAX
            return redirect(request.path + "#contact")
        else:
            # Invalid form
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"status": "error", "message": "Invalid form data", "errors": form.errors}, status=400)

            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    return render(request, "index.html", {"form": form})
def index(request):
    return HttpResponse("hello world")