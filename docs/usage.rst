=====
Usage
=====

To use django-signoff in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'signoff.apps.SignoffConfig',
        ...
    )

Add django-signoff's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^signoff/', include('signoff.urls')),
        ...
    ]

If you want users to be automatically prompted to sign any documents that you
add before they can use your site, add django-signoff's middleware:

.. code-block:: python

    MIDDLEWARE = (
       ...
       'signoff.middleware.ConsentMiddleware',
       ...
    )
