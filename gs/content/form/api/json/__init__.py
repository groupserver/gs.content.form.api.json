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
from __future__ import absolute_import, unicode_literals
from gs.content.form.base import SiteForm
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
