=======================================
:mod:`gs.content.form.api.json` Example
=======================================

Like all forms, a JSON API endpoint is made up of a schema_, some
`Python code`_, and some `ZCML configuration`_. `Testing the
form`_ is likewise fairly simple.

Schema
======

The schema for a form is just like any other. The one below makes
use of :class:`gs.auth.token.AuthToken`.

.. code-block:: python

    from __future__ import unicode_literals
    from zope.interface import Interface
    from gs.auth.token import AuthToken


    class IEthelTheFrog(Interface):
        'Get the digest groups'
        token = AuthToken(
            title='Token',
            description='The authentication token',
            required=True)

Python code
===========

Below is the Python code for a simple API endpoint.

.. code-block:: python
   :linenos:   

    class EthelTheFrogAPI(GroupEndpoint):
        label = 'POST data to this URL get info about Ethel the Frog.'
        form_fields = form.Fields(IEthelTheFrog, render_context=False)

        def __init__(self, group, request):
            super(EthelTheFrogAPI, self).__init__(group, request)

        @form.action(label='Info', name='info', prefix='', 
                     failure='info_failure')
        def info_success(self, action, data):
          r = {'show': 'Ethel the frog',
               'topic': 'The violence of British gangland', }
          retval = json.dumps(r, indent=4)
          return retval

    def info_failure(self, action, data, errors):
        return self.build_error_response(action, data, errors)

.. currentmodule:: gs.content.form.api.json

The :class:`EthelTheFrogAPI` is a normal :mod:`zope.formlib` form:

* The ``class`` inherits from either :class:`SiteEndpoint` or
  :class:`GroupEndpoint` (line 1)
* The ``label`` is used for feedback (line 2)
* The ``form_fields`` is standard for all :mod:`zope.formlib`
  forms (line 3)
* The ``__init__`` simply calls out to its super-class (lines 5
  and 6)

The :func:`zope.formlib.action` decorator for the
:func:`EthelTheFrogAPI.info_success` method (lines 8 and 9) is
slightly different to what is normally used in GroupServer,
because the ``prefix`` is set to an empty string. This is because
the ``prefix`` for all fields for a JSON form is set to an empty
string. (For a standard form the prefix is ``form.``

The return value of the success-handler is converted to a string
using the :func:`json.dumps` function (line 13) — while the
error-case is entirely handled by
:func:`EndpointMixin.build_error_response` (line 17).

ZCML configuration
==================

The ZCML for the form is likewise quite standard, providing a
name and location for the form.

.. code-block:: xml

  <browser:page
    name="ethel-the-frog.html"
    for="Products.GSContent.interfaces.IGSSiteFolder"
    class=".api.EthelTheFrogAPI"
    permission="zope2.Public"/>

Testing the Form
================

The form can be made by making a ``GET`` request to the form::

     http://gstest:8080/ethel-the-frog.html?info=&token=fake

The action-name (``info``) is provided as part of the request, as
is each field. The fields and actions do not have any prefix.

Making a post from jQuery
=========================

One of the big uses of a JSON endpoint is to allow JavaScript
code to more easily interact with the system. The form-data is
created using a :js:class:`FormData` class. The values of the
form, including the action, are added to the form, and then
:js:func:`jQuery.ajax` is used to send the data to the system.

.. code-block:: JavaScript

    function send_request() {
        var d=null, settings=null;

        d = new FormData();
        d.append('token', get_token());
        // The ID of the button that was "clicked", for zope.formlib
        d.append('submit', '');
        settings = {
            accepts: 'application/json',
            async: true,
            cache: false,
            contentType: false,
            crossDomain: false,
            data: d,
            dataType: 'json',
            error: error,
            headers: {},
            processData: false,  // No jQuery, put the data down.
            success: success,
            traditional: true,
            // timeout: TODO, What is the sane timeout?
            type: 'POST',
            url: get_ethel_url(),
        };
        jQuery.ajax(settings);
    }
