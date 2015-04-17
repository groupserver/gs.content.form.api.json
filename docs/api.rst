===================================
:mod:`gs.content.form.api.json` API
===================================
.. currentmodule:: gs.content.form.api.json

Design
======

- All responses from :class:`SiteEndpoint` or
  :class:`GroupEndpoint` pages are 
  :mimetype:`application/json`.

- Those who make a non-submission request to a
  :class:`SiteEndpoint` or :class:`GroupEndpoint` page will
  receive a response that documents the purpose, actions, and
  parameters of the endpoint. The purpose is based on the label
  attribute borrowed from :mod:`zope.formlib`. The actions are
  based on the use of the :func:`zope.formlib.form.action`
  decorator in the subclass. The documentation of parameters is
  based on the form's schema.

- Validation of submissions to :class:`SiteEndpoint` or
  :class:`GroupEndpoint` will actually check that the submitted
  data includes all required parameters.

- :class:`SiteEndpoint` and :class:`GroupEndpoint` include a 
  helper method to generate a json response for submissions that
  generate validation errors.

Using :class:`SiteEndpoint` and :class:`GroupEndpoint`
======================================================

Where possible, I've tried to make subclassing
:class:`SiteEndpoint` or :class:`GroupEndpoint` as similar to
subclassing :class:`gs.content.form.base.SiteForm` or
:class:`gs.group.form.GroupForm` as possible.

Subclasses of :class:`SiteEndpoint` or :class:`GroupEndpoint`
should use the same :func:`zope.formlib.action decorator` as
subclasses of :class:`gs.content.form.base.SiteForm` or
:class:`gs.group.form.GroupForm` to name the methods that handle
validation success and failure.

The following attribute from :mod:`zope.formlib` has a slightly
different use on a :class:`SiteEndpoint` or
:class:`GroupEndpoint` page than a
:class:`gs.content.form.base.SiteForm` or
:class:`gs.group.form.GroupForm` page:

``label``:
  A documentation string that is displayed to those who request
  the page without submitting data.

Finally, scripts submitting data to a :class:`SiteEndpoint` or
:class:`GroupEndpoint` endpoint will need to include a parameter
that indicates which action they are submitting. These actions
are listed when non-submitting request is made to the endpoint.

API
---

An page that implements a JSON API object will usually implement
a :class:`GroupEndpoint` or :class:`SiteEndpoint`. Both classes
inherit from :class`EndpointMixin`.

.. autoclass:: EndpointMixin
   :members: build_error_response
   :special-members: __call__

.. class:: GroupEndpoint(group, request)

   An endpoint for a JSON API request for a group.

   :param group: The group.
   :param request: The request object.

   .. attribute:: groupInfo

      Information about the group.


   .. attribute:: siteInfo

      Information about the site.

.. class:: SiteEndpoint(site, request)

   An endpoint for a JSON API request for a site.

   :param site: The site.
   :param request: The request object.

   .. attribute:: siteInfo

      Information about the site.

Example
=======

.. code-block:: python

    class FooAPI(GroupEndpoint):
        label = 'POST data to this URL to foo a member.'

        def __init__(self, group, request):
            super(FooAPI, self).__init__(group, request)

        @formlib.action(label='Foo', prefix='', 
                        failure='foo_failure')
        def foo_success(self, action, data):
          r = self.do_the_foo()
          retval = to_json(r, indent=4)
          return retval

    def foo_failure(self, action, data, errors):
        return self.build_error_response(action, data, errors)

