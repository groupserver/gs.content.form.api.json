# -*- coding: utf-8 -*-
from __future__ import absolute_import
from gs.content.form.form import SiteForm
from gs.group.base.form import GroupForm
from .endpoint_mixin import EndpointMixin


class SiteEndpoint(EndpointMixin, SiteForm):
    """
        JSON returning version of SiteForm, intended for the creation of API
        endpoints.
    """
    pass


class GroupEndpoint(EndpointMixin, GroupForm):
    """
        JSON returning version of GroupForm, intended for the creation of API
        endpoints.
    """
    pass
