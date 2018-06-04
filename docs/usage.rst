=====
Usage
=====

To use django-signoff in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_signoff.apps.DjangoSignoffConfig',
        ...
    )

Add django-signoff's URL patterns:

.. code-block:: python

    from django_signoff import urls as django_signoff_urls


    urlpatterns = [
        ...
        url(r'^', include(django_signoff_urls)),
        ...
    ]
