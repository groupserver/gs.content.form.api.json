# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 E-Democracy.org and Contributors.
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
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.content.form.api.json',
    version=version,
    description="Classes to make JSON based API endpoints based on Forms",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 1 - Planning",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      'License :: OSI Approved :: Zope Public License',
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='',
    author='Bill Bushey',
    author_email='bill.bushey@e-democracy.org',
    url='http://www.e-democracy.org/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.content', 'gs.content.form',
                        'gs.content.form.api'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.cachedescriptors',
        'zope.schema',
        'zope.formlib',
        'Zope2',
        'gs.content.form',
        'gs.group.base',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
