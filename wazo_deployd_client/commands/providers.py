# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import json

from xivo_lib_rest_client import RESTCommand


class ProvidersCommand(RESTCommand):

    resource = 'tenants'
    _headers = {'Accept': 'application/json'}

    def list_providers_for_tenant(self, tenant_uuid):
        response = self.session.get(
            self._providers_all_url(tenant_uuid),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def create_provider_for_tenant(self, tenant_uuid, provider_data):
        response = self.session.post(
            self._providers_all_url(tenant_uuid),
            data=json.dumps(provider_data),
            headers=self._headers,
        )
        if response.status_code != 201:
            self.raise_from_response(response)

        return response.json()

    def get_provider_for_tenant(self, tenant_uuid, provider_uuid):
        response = self.session.get(
            self._providers_one_url(tenant_uuid, provider_uuid),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def update_provider_for_tenant(self, tenant_uuid, provider_uuid, provider_data):
        response = self.session.put(
            self._providers_one_url(tenant_uuid, provider_uuid),
            data=json.dumps(provider_data),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def delete_provider_for_tenant(self, tenant_uuid, provider_uuid):
        response = self.session.delete(
            self._providers_one_url(tenant_uuid, provider_uuid),
            headers=self._headers,
        )
        if response.status_code != 204:
            self.raise_from_response(response)

    def _providers_all_url(self, tenant_uuid):
        return '{base_url}/{tenant_uuid}/providers'.format(
            base_url=self.base_url,
            tenant_uuid=tenant_uuid,
        )

    def _providers_one_url(self, tenant_uuid, provider_uuid):
        return '{base_url}/{provider_uuid}'.format(
            base_url=self._providers_all_url(tenant_uuid),
            provider_uuid=provider_uuid,
        )
