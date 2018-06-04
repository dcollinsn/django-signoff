=============================
django-signoff
=============================

.. image:: https://badge.fury.io/py/django-signoff.svg
    :target: https://badge.fury.io/py/django-signoff

.. image:: https://travis-ci.org/dcollinsn/django-signoff.svg?branch=master
    :target: https://travis-ci.org/dcollinsn/django-signoff

.. image:: https://codecov.io/gh/dcollinsn/django-signoff/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcollinsn/django-signoff

Present users with your Terms of Service and other documents, and record their consent

Documentation
-------------

The full documentation is at https://django-signoff.readthedocs.io.

Quickstart
----------

Install django-signoff::

    pip install django-signoff

Add it to your `INSTALLED_APPS`:

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

If you want users to be automatically prompted to sign any documents that you
add before they can use your site, add django-consent's middleware:

.. code-block:: python

    MIDDLEWARE = (
       ...
       'django-consent.middleware.ConsentMiddleware',
       ...
    )

You can add some settings to your settings.py file to configure django-consent:

.. code-block:: python

    # Send a notification to the user by email (using django-mailer) when they
    # sign a document, including the text of the document. Default is False.
    CONSENT_EMAIL_USER = True

    # Send a notification to a defined list of addresses whenever any user
    # signs a document (may be useful for recordkeeping). Default is none.
    CONSENT_EMAIL_RECEIPT = ['legal@example.com', ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
