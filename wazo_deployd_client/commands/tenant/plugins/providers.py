# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import json

from wazo_deployd_client.command import DeploydCommand


class PlatformsSubcommand(DeploydCommand):

    resource = 'platforms'
    _headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, client, base_url):
        super().__init__(client)
        self.base_url = base_url

    def list(self):
        response = self.session.get(
            self._providers_platforms_url(),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def _providers_platforms_url(self):
        return '{base_url}/platforms'.format(
            base_url=self.base_url,
        )


class ProvidersCommand(DeploydCommand):

    resource = 'providers'
    _headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, client):
        super().__init__(client)
        self.platforms = PlatformsSubcommand(
            client, self.base_url,
        )

    def list(self):
        url = self._providers_all_url()
        response = self.session.get(
            url,
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def create(self, provider_data):
        response = self.session.post(
            self._providers_all_url(),
            data=json.dumps(provider_data),
            headers=self._headers,
        )
        if response.status_code != 201:
            self.raise_from_response(response)

        return response.json()

    def get(self, provider_uuid):
        response = self.session.get(
            self._providers_one_url(provider_uuid),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def update(self, provider_uuid, provider_data):
        response = self.session.put(
            self._providers_one_url(provider_uuid),
            data=json.dumps(provider_data),
            headers=self._headers,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()

    def delete(self, provider_uuid):
        response = self.session.delete(
            self._providers_one_url(provider_uuid),
            headers=self._headers,
        )
        if response.status_code != 204:
            self.raise_from_response(response)

    def _providers_all_url(self):
        return self.base_url

    def _providers_one_url(self, provider_uuid):
        return '{base_url}/{provider_uuid}'.format(
            base_url=self._providers_all_url(),
            provider_uuid=provider_uuid,
        )


class TenantAwareProvidersCommand(ProvidersCommand):

    def __init__(self, client, tenant_uuid):
        super().__init__(client)
        self._headers = super()._headers
        self._headers['Wazo-Tenant'] = tenant_uuid
