# Copyright 2017-2019 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import DeploydError
from .exceptions import DeploydServiceUnavailable
from .exceptions import InvalidDeploydError


class DeploydCommand(RESTCommand):

    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    _ro_headers = {'Accept': 'application/json'}

    def ro_headers(self, **kwargs):
        return self._get_headers(rw=False, **kwargs)

    def rw_headers(self, **kwargs):
        return self._get_headers(rw=True, **kwargs)

    def _get_headers(self, tenant_uuid=None, rw=False, **ignore):
        headers = dict(self._rw_headers) if rw else dict(self._ro_headers)
        tenant_uuid = tenant_uuid or self._client.configured_tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        return headers


    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise DeploydServiceUnavailable(response)

        try:
            raise DeploydError(response)
        except InvalidDeploydError:
            RESTCommand.raise_from_response(response)
