# -*- coding: utf-8 -*-
import json
from zope.cachedescriptors.property import Lazy
from gs.group.base.form import GroupForm
from zope.schema import getFieldsInOrder
from zope.schema._bootstrapinterfaces import RequiredMissing
from zope.formlib.interfaces import WidgetInputError
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

VALIDATION_ERROR = 100


class GroupEndpoint(GroupForm):
    pageTemplateFileName = 'browser/templates/api_json_about.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, group, request):
        super(GroupEndpoint, self).__init__(group, request)
        self.prefix = ''

    @Lazy
    def endpoint_parameters(self):
        """ The list of parameters for this endpoint"""
        assert self.interface
        for name, value in getFieldsInOrder(self.interface):
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
        retval = super(GroupEndpoint, self).validate(action, data)

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
        retval = super(GroupEndpoint, self).__call__()
        self.request.response.setHeader('Content-Type', 'application/json')
        return retval
