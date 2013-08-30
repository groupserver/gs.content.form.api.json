==============================
``gs.content.form.api.json``
==============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Classes to make JSON based API endpoints based on GroupServer Forms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Bill Bushey`_
:Contact: Bill Bushey <bill.bushey@e-democracy.org>
:Date: 2013-08-30
:Organization: `E-Democracy.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0`_
  by `E-Democracy.org`_.

Introduction
===========

This egg provides classes which can be used to make JSON returning API
endpoints that use the schema interfaces and validation code of zope.formlib
forms.

Currently this egg provides one class: GroupEndpoint.

Features of GroupEndpoint
=========================

 - All responses from GroupEndpoint pages are application/json.
 - Those who make a non-submission request to a GroupEndpoint page will
receive a response that documents the purpose and parameters of the endpoint.
The purpose is based on the label attribute borrowed from zope.formlib, and the
documentation of parameters is based on the form's schema.
 - Validation of submissions to GroupEndpoint will actually check that the
submitted data includes all required parameters.
- GroupEndpoint includes a helper method to generate a json response for
submissions that generate validation errors.

Using GroupEndpoint
===================

Where possible, I've tried to make subclassing GroupEndpoint as similar to
subclassing GroupForm as possible. That said, subclasses of GroupEndpoint do
need to define one attributes that subclasses of GroupForm do not:

 - interface: The interface schema of the form. It probably is possible to get
the same information out of form_fields, but in my hacking I ended up pulling
information directly from the interface.

Subclasses of GroupEndpoint should use the same zope.formlib.action decorator
as subclasses of GroupForm to name the methods that handle validation success
and failure. One important difference is that subclasses of GroupEndpoint
should set the prefix parameter of this decorator to an empty string.

The following attribute from zope.formlib has a slightly different use on a
GroupEndpoint page than a GroupForm page:

 - label: A documentation string that is displayed to those who request the 
page without submitting data.

Finally, scripts submitting data to a GroupEndpoint endpoint will need to
include the parameter 'submit' to indicate that they are submitting data
to be processed.



Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.content.form.api.json
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _E-Democracy.org: http://www.e-democracy.org
.. _Bill Bushey: http://groupserver.org/p/wbushey
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
