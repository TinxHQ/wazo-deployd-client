#!/usr/bin/env python3
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from setuptools import setup
from setuptools import find_packages


setup(
    name='wazo_deployd_client',
    version='0.1',
    description='a simple client library for the wazo deployd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_deployd_client.commands': [
            'config = wazo_deployd_client.commands.config:ConfigCommand',
            'tenant = wazo_deployd_client.commands.tenant:Tenant',
            'providers = wazo_deployd_client.commands.tenant.plugins.providers:ProvidersCommand',
            'instances = wazo_deployd_client.commands.tenant.plugins.instances:InstancesCommand',
        ],
        'wazo_deployd_client.commands.tenant.plugins': [
            'providers = wazo_deployd_client.commands.tenant.plugins.providers:TenantAwareProvidersCommand',
            'instances = wazo_deployd_client.commands.tenant.plugins.instances:TenantAwareInstancesCommand',
        ],
    }
)
