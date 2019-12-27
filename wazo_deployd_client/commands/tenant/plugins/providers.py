# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

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

    def list(self, **params):
        url = self._providers_all_url()
        response = self.session.get(
            url,
            headers=self._headers,
            params=params,
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

    def list_images(self, provider_uuid, **params):
        return self._providers_resources('images', provider_uuid, **params)

    def list_locations(self, provider_uuid, **params):
        return self._providers_resources('locations', provider_uuid, **params)

    def list_key_pairs(self, provider_uuid, **params):
        return self._providers_resources('keypairs', provider_uuid, **params)

    def list_networks(self, provider_uuid, **params):
        return self._providers_resources('networks', provider_uuid, **params)

    def list_sizes(self, provider_uuid, **params):
        return self._providers_resources('sizes', provider_uuid, **params)

    def list_subnets(self, provider_uuid, **params):
        return self._providers_resources('subnets', provider_uuid, **params)

    def list_regions(self, provider_uuid, **params):
        return self._providers_resources('regions', provider_uuid, **params)

    def _providers_all_url(self):
        return self.base_url

    def _providers_one_url(self, provider_uuid):
        return '{base_url}/{provider_uuid}'.format(
            base_url=self._providers_all_url(),
            provider_uuid=provider_uuid,
        )

    def _providers_resources(self, endpoint, provider_uuid, **params):
        url = '{base_url}/{endpoint}'.format(
            base_url=self._providers_one_url(provider_uuid),
            endpoint=endpoint
        )
        response = self.session.get(
            url,
            headers=self._headers,
            params=params,
        )
        if response.status_code != 200:
            self.raise_from_response(response)

        return response.json()


class TenantAwareProvidersCommand(ProvidersCommand):

    def __init__(self, client, tenant_uuids):
        super().__init__(client)
        self._headers = dict(self._headers)
        self._headers['Wazo-Tenant'] = ', '.join(tenant_uuids)
