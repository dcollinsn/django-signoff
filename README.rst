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

You can add some settings to your settings.py file to configure django-signoff:

.. code-block:: python

    # Send a notification to the user by email (using django-mailer) when they
    # sign a document, including the text of the document. Default is False.
    SIGNOFF_EMAIL_USER = True

    # Send a notification to a defined list of addresses whenever any user
    # signs a document (may be useful for recordkeeping). Default is none.
    SIGNOFF_EMAIL_RECEIPT = ['legal@example.com', ]

    # We don't delete signatures from your database, for compliance reasons.
    # However, we do require new signatures whenever a new version of a
    # document is created by creating a new object and setting the
    # `prev_version` field. You can also require new signatures whenever a
    # document is edited in the admin (we check the `updated` field of
    # the document, and only accept newer signatures):
    SIGNOFF_CHECK_DOCUMENT_UPDATED = True

    # You can also require new signatures whenever a user's display name
    # changes (we require users to enter their display name when signing
    # a document):
    SIGNOFF_CHECK_FULL_NAME = True

    # If you're using the middleware, it will redirect any logged-in requests
    # from users who owe signatures to the 'legal' index by default, except
    # for requests within the 'signoff' app (to avoid redirect loops), and
    # requests to the 'auth_logout' url name (to allow users to log out
    # of the site). If you want to add additional URLs that can be accessed
    # by users who have not signed your documents yet, you can do something
    # like the following:
    SIGNOFF_ADDITIONAL_ALLOWED_APPS = ('djdt', )
    SIGNOFF_ADDITIONAL_ALLOWED_URLS = ('auth_logout', )
    # (The latter is only an example, 'auth_logout' is automatically allowed.)

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
