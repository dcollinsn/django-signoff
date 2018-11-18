from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from signoff.models import DocumentConsent


@receiver(post_save, sender=DocumentConsent, dispatch_uid="consent-saved")
def handle_signoff_emails(instance, created, **kwargs):
    if not created:
        return

    message = EmailMultiAlternatives()

    # Collect recipients based on site settings
    if hasattr(settings, 'SIGNOFF_EMAIL_USER') and\
       settings.SIGNOFF_EMAIL_USER:
        message.to = [instance.user.email, ]

    if hasattr(settings, 'SIGNOFF_EMAIL_RECEIPT') and\
       settings.SIGNOFF_EMAIL_RECEIPT:
        if message.to:
            message.bcc = settings.SIGNOFF_EMAIL_RECEIPT
        else:
            message.to = settings.SIGNOFF_EMAIL_RECEIPT

    # If neither key is true, then we have no recipients, and therefore no mail
    # to send
    if not message.to:
        return

    if hasattr(settings, 'SIGNOFF_EMAIL_FROM') and\
       settings.SIGNOFF_EMAIL_FROM:
        message.from_email = settings.SIGNOFF_EMAIL_FROM

    if hasattr(settings, 'SIGNOFF_EMAIL_REPLY_TO') and\
       settings.SIGNOFF_EMAIL_REPLY_TO:
        message.reply_to = (settings.SIGNOFF_EMAIL_REPLY_TO,)

    # Build message
    template_context = {
        'document': instance.document,
        'user': instance.user,
        'instance': instance,
    }

    message.subject = render_to_string(
        'signoff/email_subject.txt',
        context=template_context,
    ).strip()

    html_body = render_to_string(
        'signoff/email_body.html',
        context=template_context,
    ).strip()

    message.body = html_body
    message.attach_alternative(html_body, 'text/html')
    message.send()
