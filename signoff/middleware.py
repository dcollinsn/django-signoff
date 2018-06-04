from django.shortcuts import redirect
from django.urls import resolve
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from signoff.models import Document


class ConsentMiddleware(MiddlewareMixin):
    """
    This middleware redirects users to sign the site's terms of service or
    other documents if they haven't done so.
    """

    def process_request(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated:
            # Check if the user is on one of our pages, if so, pass
            if resolve(request.path).app_name == 'signoff':
                return

            # Check if the user owes us any signatures, if so:
            user_owes_signatures = False
            for document in Document.objects.with_user(request.user)\
                                    .filter(next_version__isnull=True):
                if document.required_by is None or\
                   document.required_by <= timezone.now():
                    if not document.user_consents:
                        user_owes_signatures = True
            if user_owes_signatures:
                return redirect('signoff:signoff_index')
            return
