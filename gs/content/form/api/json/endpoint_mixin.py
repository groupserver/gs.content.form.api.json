# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import json
from zope.cachedescriptors.property import Lazy
from zope.schema import getFieldsInOrder
from zope.schema._bootstrapinterfaces import RequiredMissing
from zope.formlib.interfaces import WidgetInputError
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

VALIDATION_ERROR = 100

###############################################################################
# Classes that inherit EndpointMixin must have SiteForm or GroupFrom in their
# inheritance tree above EndpointMixin.
#
# The recommended way to inherit EndpointMixin is via multiple inheritance,
# with SiteForm or GroupForm inherited immediately after. E.g.:
#      class Example(EndpointMixin, SiteForm):
###############################################################################


class EndpointMixin(object):
    pageTemplateFileName = 'browser/templates/api_json_about.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, cxt, request):
        super(EndpointMixin, self).__init__(cxt, request)
        self.prefix = ''

    @Lazy
    def interfaces(self):
        """The set of schema interfaces used by this endpoint"""
        assert self.form_fields
        retval = set([field.interface for field in self.form_fields])
        return retval

    @property
    def endpoint_parameters(self):
        """ The list of parameters for this endpoint"""
        for interface in self.interfaces:
            for name, value in getFieldsInOrder(interface):
                yield ({"name": name, "value": value})

    @Lazy
    def required_endpoint_parameters(self):
        """ The list of required parameters for this endpoint"""
        for endpoint_parameter in self.endpoint_parameters:
            if endpoint_parameter['value'].required:
                yield endpoint_parameter

    def validate(self, action, data):
        # Super's validate method does not actually check that all required
        # fields are present in the posted data.

        retval = super(EndpointMixin, self).validate(action, data)

        missing_required_params = [parameter for parameter in
                                   self.required_endpoint_parameters
                                   if parameter['name'] not in data]
        for missing_required_param in missing_required_params:
            retval.append(WidgetInputError(missing_required_param['name'],
                          missing_required_param['value'].title,
                          RequiredMissing(missing_required_param['name'])))
        return retval

    def build_error_response(self, action, data, errors):
        retdict = {
            'status': VALIDATION_ERROR,
            'message': [unicode(error) for error in errors]
        }
        retval = json.dumps(retdict, indent=4)
        return retval

    def __call__(self, ignore_request=False):
        retval = super(EndpointMixin, self).__call__()
        self.request.response.setHeader('Content-Type', 'application/json')
        return retval
