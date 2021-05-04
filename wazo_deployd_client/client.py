# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from wazo_lib_rest_client.client import BaseClient


class DeploydClient(BaseClient):

    namespace = 'wazo_deployd_client.commands'

    def __init__(self, host, port=443, prefix='/api/deployd', version='0.1', **kwargs):
        super(DeploydClient, self).__init__(
            host=host,
            port=port,
            prefix=prefix,
            version=version,
            **kwargs,
        )

    # this function replicates the tenant method of the BaseClient
    # which is overridden by the tenant command
    def configured_tenant(self):
        return self._tenant_id or self._default_tenant_id
