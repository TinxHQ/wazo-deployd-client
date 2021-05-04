#!/usr/bin/env python3
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

TENANT_MODULE = 'wazo_deployd_client.commands.tenant.plugins'

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
            f'instances = {TENANT_MODULE}.instances:InstancesCommand',
            f'providers = {TENANT_MODULE}.providers:ProvidersCommand',
            'status = wazo_deployd_client.commands.status:StatusCommand',
            'tenant = wazo_deployd_client.commands.tenant:Tenant',
        ],
        'wazo_deployd_client.commands.tenant.plugins': [
            f'providers = {TENANT_MODULE}.providers:TenantAwareProvidersCommand',
            f'instances = {TENANT_MODULE}.instances:TenantAwareInstancesCommand',
        ],
    },
)
