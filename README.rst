========================
django-eml-email-backend
========================

Django has filebased email backend that is handy for inspecting
outgoing emails during development. But this backend saves emails
to '.log' files and it is not clear how to view them in email client.
This is especially important for html emails.

eml_email_backend saves outgoing emails to '.eml' files. This way emails
can be opened directly in MS Outlook or Mail.app or previewed
in OS X Finder by simply pressing space over the file.

Installation
============

::

    $ pip install django-eml-backend

Usage
=====

Setup the django email backend in your local_settings.py::

    EMAIL_BACKEND = 'eml_email_backend.EmailBackend'
    EMAIL_FILE_PATH = 'path/to/output/folder/'


Limitations
===========

Full eml format is not supported, file extensions are just changed
from ".log" to ".eml" by this app. It works in most cases. Patches
for better eml support are welcome.

See also: https://code.djangoproject.com/ticket/15793
