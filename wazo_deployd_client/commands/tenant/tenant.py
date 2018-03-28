# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from stevedore import extension

logger = logging.getLogger(__name__)

plugin_names = set()


class Tenant(object):
    """Proxy class for calling resources that need tenant infos"""

    namespace = 'wazo_deployd_client.commands.tenant.plugins'

    def __init__(self, client):
        self._client = client
        self._load_plugins()

    def __call__(self, *tenant_uuids):
        self.tenant_uuids = tenant_uuids
        return self

    def __getattribute__(self, name):
        attribute = super().__getattribute__(name)
        if name in plugin_names:
            return attribute(self._client, self.tenant_uuids)
        return attribute

    def _load_plugins(self):

        def set_extension_instance_as_attribute(extension_):
            setattr(self, extension_.name, extension_.plugin)
            plugin_names.add(extension_.name)

        extension_manager = extension.ExtensionManager(
            self.namespace,
        )
        try:
            extension_manager.map(set_extension_instance_as_attribute)
        except RuntimeError:
            logger.warning('No commands found')
