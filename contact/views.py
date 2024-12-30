from time import sleep
import logging
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from smtplib import SMTPException as EmailServiceError
from Xarale import settings
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import SubscriberForm
logger = logging.getLogger(__name__)

def validate_email_address(email):
    """
    Validates email format using Django's built-in validator.
    Returns (is_valid, error_message) tuple.
    """
    validator = EmailValidator()
    try:
        validator(email)
        return True, None
    except ValidationError:
        return False, "Invalid email format"

def check_email_service_connection():
    """
    Verifies connection to email service.
    In production, this could ping SMTP server or perform other checks.
    """
    try:
        # Simple test email to verify service
        send_mail(
            subject="Test Connection",
            message="Test",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        return True
    except (EmailServiceError, BadHeaderError):
        return False

def contact(request):
    if request.method == "POST":
        try:
            # Extract form data with default values to prevent None
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            subject = request.POST.get('subject', '').strip()
            message = request.POST.get('message', '').strip()

            # Validate required fields
            if not all([name, email, subject, message]):
                logger.warning("Missing required fields in contact form submission")
                return JsonResponse({
                    'status': 'error',
                    'message': 'All fields are required'
                }, status=400)

            # Validate email format
            is_valid_email, error_message = validate_email_address(email)
            if not is_valid_email:
                logger.warning(f"Invalid email format: {email}")
                return JsonResponse({
                    'status': 'error',
                    'message': error_message
                }, status=400)

            # Check email service before attempting to send
            if not check_email_service_connection():
                logger.error("Email service connection check failed")
                return JsonResponse({
                    'status': 'error',
                    'message': 'Email service temporarily unavailable'
                }, status=503)

            # Prepare email content
            email_subject = f"Contact Form: {subject}"
            email_message = (
                f"Contact Form Submission\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message}"
            )

            # Attempt to send email with retries
            retry_count = 3
            last_error = None
            
            while retry_count > 0:
                try:
                    send_mail(
                        subject=email_subject,
                        message=email_message,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=['samuelokwu85@gmail.com'],
                        fail_silently=False,
                    )
                    logger.info(f"Successfully sent contact form email from {email}")
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Your message has been sent successfully'
                    })
                    
                except (EmailServiceError, BadHeaderError) as e:
                    last_error = str(e)
                    retry_count -= 1
                    if retry_count > 0:
                        logger.warning(f"Email sending failed, attempts remaining: {retry_count}. Error: {last_error}")
                        sleep(1)  # Wait before retrying
                    
            # If we get here, all retries failed
            logger.error(f"Failed to send email after all retries. Last error: {last_error}")
            return JsonResponse({
                'status': 'error',
                'message': 'Unable to send email at this time. Please try again later.'
            }, status=503)

        except Exception as e:
            logger.error(f"Unexpected error in contact form: {str(e)}", exc_info=True)
            return JsonResponse({
                'status': 'error',
                'message': 'An unexpected error occurred'
            }, status=500)

    # Handle GET request
    return render(request, 'contact.html')




@csrf_exempt  # Exempt only if you're managing CSRF in your JavaScript
def subscribe(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Thank you for subscribing!'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'message': 'Invalid email address.', 'errors': errors})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
