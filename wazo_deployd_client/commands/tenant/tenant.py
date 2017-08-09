# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from stevedore import extension

logger = logging.getLogger(__name__)

plugin_names = set()


class Tenant(object):
    """Proxy class for calling resources that starts with /tenants/<uuid>"""

    namespace = 'wazo_deployd_client.commands.tenant.plugins'

    def __init__(self, client):
        self._client = client
        self._load_plugins()

    def __call__(self, tenant_uuid):
        self.tenant_uuid = tenant_uuid
        return self

    def __getattribute__(self, name):
        attribute = super().__getattribute__(name)
        if name in plugin_names:
            attribute.tenant_uuid = self.tenant_uuid
        return attribute

    def _load_plugins(self):

        def set_extension_instance_as_attribute(extension_):
            setattr(self, extension_.name, extension_.obj)
            plugin_names.add(extension_.name)

        extension_manager = extension.ExtensionManager(
            self.namespace,
            invoke_on_load=True,
            invoke_args=(self._client,),
        )
        try:
            extension_manager.map(set_extension_instance_as_attribute)
        except RuntimeError:
            logger.warning('No commands found')
